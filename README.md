# passwdgen
Generates a statistically strong password with a minimum char length of your choice.

A strong password should be of decent length, e.g. 10-20+ characters long, containing alphanumeric characters both up and lower case with a special characters. This script however, does not includ special characters.

A strong password should also not be a word or phrase that either has a personal attachment (name, pets name, home city) and it should also not follow a logical flow e.g. 'theSleepingDog' as it's more likely to be comprimised by a dictionary attack.

This script solves these problems by generating a password greater than your chosen minimum length of X amount of random words from the word list provided whilst adding 2 random digits to the end. Although this is not necessarily the 'perfect' system, it will non-the-less create a very strong password that is very unlikely to succumb to any dictionary attack.

Usage

<code>$python passwdgen.py 20</code>

Output:

<code>breachingunevenlypolyglot26</code>

(highly unlikely to be in dictionary attack and easy to remember)
