# passwdgen
Generates a statistically strong password with a minimum char length of your choice.

A strong password should be of decent length, e.g. 10-20+ characters long, containing alphanumeric characters both up and lower case with special characters. This script however, does not includ special characters.

A strong password should also not be a word or phrase that either has a personal attachment (name, pets name, home city) and it should also not follow a logical flow e.g. 'theSleepingDog' as it's more likely to be comprimised by a dictionary attack.

This script solves these problems by generating a password of your chosen length with X amount of random words from the word list provided whilst adding at least 2 random digits either before of after each word (percentage chance). Although this is not necessarily the 'perfect' system, it will, non-the-less, create a very strong password that is very unlikely to succumb to any dictionary attack.

Usage

<code>$python passwdgen.py 20</code>

Sample Outputs:

<code>Hydroplanes27Spitted</code>
<code>UnawaresShaverRaft25</code>
<code>76ScarvesBrittSticks</code>
<code>LandmassColoration58</code>
<code>Stile66BlockSmothers</code>
<code>HillierIncarnation20</code>
<code>10Vaults58Ghosting93</code>
<code>60Joyriders37Lyric54</code>
<code>OverhungTilted26Lief</code>
<code>83HawkingSunblocks83</code>
<code>82Brady48Middlebrows</code>
<code>Misjudging62Implicit</code>
<code>InfringedDemarcate30</code>
<code>96UnfeelinglyAviator</code>
<code>SaabGunners77Goner15</code>
<code>RobustWards32Dirtied</code>
<code>FellerHomesteaders11</code>
<code>Kettledrums27Guzzler</code>
<code>Graders5225Izhevsk64</code>

(highly unlikely to be in dictionary attack and easy to remember)
