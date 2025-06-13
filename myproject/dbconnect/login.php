<?php
    include_once ("dbconnect/connect.php");
    if (isset($_POST['submit'])) {
        $name = $_POST['name'];
        $password = $_POST['password'];


        try {
            $sql = "SELECT * FROM `users` WHERE 1 name= '$name', password=$password";

            $result = $conn->query($sql);

            $row = mysqli_num_rows($result);

            if ($row) {
                echo "<script>alert('login successfull');</script>";
                header("location: home.php");
            } else {
                echo "<script>alert('Error');</script>";
                header("location : index.php");
            }

        }catch(mysqli_sql_exception $e){
            echo $e->getMessage();
        }
    }
?>
