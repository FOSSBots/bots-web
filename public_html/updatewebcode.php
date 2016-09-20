<?php>
shell_exec ("ssh zppix1@dev.tools.wmflabs.org");
sleep("15");
shell_exec ("sudo -iu tools.zppixbot");
sleep("6");
shell_exec ("git pull");
?php>
<script type="text/javascript"]>
window.alert("Complete");
</script>