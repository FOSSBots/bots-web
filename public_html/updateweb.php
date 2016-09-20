
<?php
if ($_GET['run']) {
  # This code will run if ?run=true is set.
  exec("/data/project/zppixbot/public_html/updatewebcode.php");
    exec("/data/project/zppixbot/public_html/gitcommitauto.php");
}
?>
<a href="?run=true">Update website and commit changes</a>
