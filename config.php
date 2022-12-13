<?php

$url = 'http://localhost:8069';
$db = "db_01";
    $username = "db_01";
    $password = "db_01";

require_once('ripcord/>ripcord.php');
//require ('ripcord.ripcord.php');
$common = Ripcord::client ($url . '/xmlrpc/2/common');

//$common = ripcord::client($url."/xmlrpc/2/common");
$uid = $common->authenticate($db, $username, $password, array());

$ver = $common->version();
echo($ver);

?>
