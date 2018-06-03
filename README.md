# suricata-prettifier

Snake-powered pipe cleaner eats single-line Suricata rules and poops out pleasantly-spaced, vibrantly-coloured delicacies straight to your plate. Examine this exemplary example:

```
alert tcp $HOME_NET any -> 94.242.238.242 6565 (msg:"EmergingThreats:Indicator-2405101"; flow:to_server,established; flags:S; reference:url,doc.emergingthreats.net/bin/view/Main/BotCC; reference:url,www.shadowserver.org; threshold: type limit, track by_src, seconds 360, count 1; classtype:trojan-activity; flowbits:set,ET.Evil; flowbits:set,ET.BotccIP; sid: 533; rev:4991;)
```

Now watch as the snake-babies devour such fine a morsel – the last food for winter – then travel northward to return to their mates, leaving behind their season's work:

![Snake poop](https://user-images.githubusercontent.com/33840/40883915-2600beee-66d6-11e8-9e94-97b7730ebb62.png)

```
alert tcp $HOME_NET any -> 94.242.238.242 6565 ( \
  msg: "EmergingThreats:Indicator-2405101"; \
  flow: to_server,established; \
  flags: S; \
  reference: url,doc.emergingthreats.net/bin/view/Main/BotCC; \
  reference: url,www.shadowserver.org; \
  threshold: type limit, track by_src, seconds 360, count 1; \
  classtype: trojan-activity; \
  flowbits: set,ET.Evil; \
  flowbits: set,ET.BotccIP; \
  sid: 533; \
  rev: 4991; \
)
```

Note: options with line continuations tested working with Suricata 4.0.4


# Installation

```bash
pip install suricata-prettifier
```


# Usage

Highlight and format right in your console. Wow.

```bash
prettify-suricata input.rules
```

Use it to generate sweet posts for your LiveJournal (Netscape Navigator required to view)

```bash
prettify-suricata -f html input.rules input.formatted.html style=vim full=True
```

Read from stdin and write to stdou to create your own pipe dream

```bash
head -n 50 input.rules | prettify-suricata -f html - - style=vim full=True | tee input.formatted.html
```
