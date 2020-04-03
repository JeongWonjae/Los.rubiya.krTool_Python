<?php
  $a="plzplzplzplzplzplzplzplzplz";
  $c="B9E5AD34D653A31A0720B840328FC6DC292E67DC316E959865CA79BCF90CD9F1E4BED09A1EF5072AA5680363D8DB04910239AF5F166D760005A626EBA6CF1AE2CF96F2B92328529C972D0666C1909D00FA544F2F2CE6A5A815E1697A1A24A71080F95E797A999730AE2EC0039C0277E467BFB533";
  $url="http://testaspnet.vulnweb.com/Comments.aspx?id=30";
  $d=array("tbComment"=>$a, "btnSend"=>"Send+comment");

  function post($url, $d, $c)
  {
    $ch=curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    $headers=[
      "Host: testaspnet.vulnweb.com",
      "Cache-Control: max-age=0",
      "Origin: http://testaspnet.vulnweb.com",
      "Upgrade-Insecure-Requests: 1",
      "Content-Type: application/x-www-form-urlencoded",
      "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
      "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Accept-Encoding: gzip, deflate",
      "Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
      "Cookie: frmLogin= ".$c,
      "Connection: close"
    ];
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($d));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);

    $response=curl_exec($ch);
    $hc=curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return $hc.$response;
  }

  echo post($url, $d, $c);

?>
