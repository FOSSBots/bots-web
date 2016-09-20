<?php>
shell_exec ("ssh zppix1@dev.tools.wmflabs.org");
sleep("15");
shell_exec ("sudo -iu tools.zppixbot");
sleep("6");
shell_exec ("git commit -m Automatic changes sync from website, do not revert.");
?php>