<?php
$cne = $_POST['CNE'];
$date_examen = $_POST['date'];
$salle = $_POST['salles'];

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
echo $uid;
//var_dump($ver);

$models = ripcord::client("$url/xmlrpc/2/object");

//on recupere l'id de l'etudiant recupere par le scan

$var_etud = $models->execute_kw($db, $uid, $password,
    'etudiant', 'search',
    array(array(array('cne','=',$cne)))
);
//var_dump($var_etud);

// on recupere l'id de la salle choisi

$var_salle = $models->execute_kw($db, $uid, $password,
    'local', 'search_read',
    array(array(array('nom','=',$salle)))
);
var_dump($var_salle);
$id_salle = $var_salle[0]['id'];

echo $id_salle;

// $var_exam = $models->execute_kw($db, $uid, $password,
//     'examen', 'search_read',
//     array(array(array(array('salle','=',$salle)))
// ));
// var_dump($var_exam);

// $id_exam = $var_exam[0]['id'];

// echo $id_exam;


// on recupere l'id de l'examen qui correspond à la date choisi et à la salle selectionnée
$var_examen = $models->execute_kw($db, $uid, $password,
    'examen', 'search_read',
    array(array(array('date','=',"$date_examen"),array('local_id','=',$id_salle)))
);
var_dump($var_examen);

$id_examen = $var_examen[0]['id'];

echo $id_examen;





$etud = $models->execute_kw($db, $uid, $password,
    'etudiant', 'read',
    array($var_etud) 
);
////var_dump($etud);

$id_etud = $etud[0]['id'];


//  on cherche le pointage qui correspond à l'id etud recupere precedemment et l'id examen aussi
$pointage = $models->execute_kw($db, $uid, $password,
    'pointage', 'search_read',
    array(array(array('etudiant_id','=',$id_etud),array('examen_id','=',$id_examen)))
);

//var_dump($pointage);
echo $pointage[0]['id'];

$salles =$models->execute_kw($db, $uid, $password,
    'local', 'search_read',
    array());
var_dump($salles);


// on fait le pointage
$models->execute_kw($db, $uid, $password,
    'pointage', 'write',
    array(array($pointage[0]['id']),array('state'=>"present"))

);
if($models){
echo "Pointage réussi de l'etudiant de CNE :".$cne;
}

//var_dump($pointer);





// $models->execute_kw($db, $uid, $password,
//     'examen', 'unlink',
//     array(array(3))
// );
// echo $id[0]['id_examen'];


// $record=  $models->execute_kw($db, $uid, $password,
//     'examen', 'read',
//     array($var));
    

// var_dump($record);

// $models->execute_kw($db, $uid, $password,
//     'res.partner', 'search', array(
//         array(array('is_company', '=', true),
//               array('customer', '=', true))));

// $ids=$models->execute_kw($db, $uid, $password,
//     'res.partner', 'search',
//     array(array(array('is_company', '=', true),
//     array('limit'=>1)
//                 )));
  

// $models->execute_kw($db, $uid, $password,
//     'res.partner', 'fields_get',
//     array(), array('attributes' => array('name', 'date', 'title'),
//      array('offset'=>10,'limit'=>5)
// ));

// $var=$models->execute_kw($db, $uid, $password,
//     'res.partner', 'read',
//     array($ids),
//     array('fields'=>array('name', 'country_id', 'comment')));

// var_dump($var); 
?>
