<?php
// require('C:\wamp64\bin\php\php8.1.0\vendor\autoload.php');

// use Zxing\QrReader;

// $msg="";

//  if(isset($_POST['upload'])){
 
//   $filename = $_FILES["picture"]["name"];
//   $filetype = $_FILES["picture"]["type"];
//   $filetemp = $_FILES["picture"]["tmp_name"];
//   $filesize = $_FILES["picture"]["size"];

//    $filetype = explode("/",$filetype );

//    if($filetype[0] !== "image"){
//      $msg = "file is invalid". $filetype;
//    }
//    else{

//     move_uploaded_file($filetemp,"images/". $filename); 
//     $qrScan = new QrReader("images/". $filename);
//     $msg = "QR is scanned and the result is  ". $qrScan->text();
//    }

//   }
 

?>
      <?php

$url = 'http://localhost:8069';
$db = "db_01";
    $username = "db_01";
    $password = "db_01";

require_once('ripcord/ripcord.php');
//require ('ripcord.ripcord.php');
$common = ripcord::client ($url . '/xmlrpc/2/common');

//$common = ripcord::client($url."/xmlrpc/2/common");
$uid = $common->authenticate($db, $username, $password, array());
$ver = $common->version();
// echo $uid;
//var_dump($ver);

$models = ripcord::client("$url/xmlrpc/2/object");

        $salles =$models->execute_kw($db, $uid, $password,
    'local', 'search_read',
    array());
    ?>
   

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odoo</title>
    <script src="https://unpkg.com/html5-qrcode@2.0.9/dist/html5-qrcode.min.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</head>

<body class="p-2 m-2 col">

<h1 class="text-center"> Pointage </h1>

<div class="row  p-2 m-2 col" >



<div class=" p-2 m-1 col">
  <form class="row g-3"  action="config.php"  method="post">

   <div class="row mb-3">
    <label for="cne"  class="col-sm-2 col-form-label">CNE : </label>
    <div class="col-sm-6">
    <input type="text" class="form-control" id= "cne" name="CNE" placeholder="CNE"
    >
  </div>
  </div>
  <div class="row mb-3">
    <label for="date"  class="col-sm-2 col-form-label">Date examen : </label>
   <div class="col-sm-6">
        <input type="datetime-local" class="form-control" id =date name="date" />

  </div>
  </div>
  <div class="row mb-3">
    
    <label for="salle"  class="col-sm-2 col-form-label">Salle : </label>
     
    <div class="col-sm-6">
      <select name="salles" class="form-select" id="salles">
    <option selected>Choisir salle...</option>

     <?php
    // var_dump($salles);
    foreach($salles as $s){
          echo "<option value=".$s['nom'].">".$s['nom']."</option>";
    }

      ?>
    </select>
  </div>
  </div>

  <div class="col-12">
    <button type="submit" class="btn btn-primary">Enregistrer</button>
  </div>
</form>
</div>

<div class=" col">

<div id="qr-reader" style="width: 600px"></div>

</div>

</div>
</div>





 <!-- <form action="" method="post"  enctype="multipart/form-data">
 
<input type="file" name="picture" accept="image/*" capture="camera" id="qrcode">
  <button  name="upload" type="submit">upload</button>
   
   </form> -->


</body>

<script>
  function onScanSuccess(decodedText, decodedResult) {
    console.log(`Code scanned = ${decodedText}`, decodedResult);

    document.querySelector("#cne").value=decodedText;
}
var html5QrcodeScanner = new Html5QrcodeScanner(
	"qr-reader", { fps: 10, qrbox: 250 });
html5QrcodeScanner.render(onScanSuccess);
</script>

</html>