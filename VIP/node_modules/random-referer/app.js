/*
 * random-referer
 * https://github.com/rizsyad/random-referer
 *
 * Copyright (c) 2022 Rizsyad AR
 * Licensed under the MIT license.
 */

const rand = require("random-seed").create();
const namor = require("namor");

exports.getRandom = () => {
  // create list protocol
  const protocol = ["http://", "https://"];

  // create list subdomain
  const subdomain = [
    "www.",
    "search.",
    "play.",
    "drive.",
    "jobs.",
    "add.",
    "profile.",
    "careers.",
    "taginfo.",
    "engadget.",
    "developers.",
    "api.",
    "my.",
    "dashboard.",
    "",
  ];

  // create list name Domain
  const domainName = [
    "google",
    "yahoo",
    "bing",
    "facebook",
    "baidu",
    "yandex",
    "usatoday",
    "duckduckgo",
    "ask",
    "vk",
    "reddit",
    "npmjs",
    "pinterest",
    namor.generate().replace(/-/g, ""),
  ];

  // create list tld
  const tld = [
    "com",
    "xyz",
    "net",
    "biz",
    "info",
    "org",
    "edu",
    "pro",
    "travel",
    "coop",
    "tv",
    "tor",
    "io",
    "asia",
  ];

  // choose one from the list
  const selectProtocol = protocol[rand.intBetween(0, protocol.length - 1)];
  const selectSubdomain = subdomain[rand.intBetween(0, subdomain.length - 1)];
  const selectTld = tld[rand.intBetween(0, tld.length - 1)];
  const slectDomainName = domainName[rand.intBetween(0, domainName.length - 1)];

  return `${selectProtocol}${selectSubdomain}${slectDomainName}.${selectTld}`;
};
