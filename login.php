<?php

// Database connection
$conn = new mysqli('localhost','root','','login_details');
$c = mysqli_connect('localhost','root', '', 'login_details');
if($conn->connect_error){
    echo "$conn->connect_error";
    die("Connection Failed : ". $conn->connect_error);
}
 else {
// name and password sent from form 
if(isset($_POST['namei']) && isset($_POST['passwordi'])){
$name=$_POST['namei']; 
$password=$_POST['passwordi']; 
}

$query = mysqli_query($c, "SELECT * FROM login WHERE hid =  '$name' and password = '$password'");
if(mysqli_num_rows($query)>0)
{
    header("Location: http://localhost:3000");
    exit;

}
else
{
    echo '<script>alert("Invalid credentials")</script>'; 
}
 }