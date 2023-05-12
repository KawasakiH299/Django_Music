<?php
header('content-type:text/html;charset=utf-8');
$host = "localhost"; //域名
$user = "root"; //账户名
$password = ""; //密码
$db = "myDB"; //数据库名


//实例化 mysqli 对象，连接 mysql 数据库
$mysqli = new mysqli($host, $user, $password, $db);
if ($mysqli->connect_errno) {
    die($mysqli->connect_error);
}
$mysqli->set_charset('utf8'); //设置字符集



//执行读取用户
getUser($mysqli);

 //读取用户并显示
function getUser($mysqli)
    {
        $sql = "SELECT username, age,gender FROM user WHERE username = ? and passwd= ?";
        $mysqli_stmt = $mysqli->prepare($sql);
        //定义要存值的变量

        $username=$_POST['username'];
        $passwd=$_POST['passwd'];
        $mysqli_stmt->bind_param('ss', $username,$passwd);


        if ($mysqli_stmt->execute()) {
            echo $mysqli_stmt->insert_id; //程序成功，返回插入数据表的行 id
            echo PHP_EOL;
            echo "<script>alert('恭喜您，登录成功！');window.location.href='../../index.html'</script>";         // 直接跳转登录页 js代码
        } else {
            echo $mysqli_stmt->error; //执行失败，错误信息
    
            // $username=null;
            // $age=null;
            // $gender=null;
            // //bind_result() 绑定结果集中的值到变量
            // $mysqli_stmt->bind_result($username, $age, $gender);
            // //遍历结果集
            // while ($mysqli_stmt->fetch()) {
            //     echo '欢迎我们尊贵的 ' . $username;
            //     echo '<br/>今年年龄:' . $age;
            //     $gender = $gender == 1 ? '男' : '女';
            //     echo "<br/>您的性别:" . $gender;
            // }
            
        }//释放结果集
    $mysqli_stmt->free_result();
    $mysqli_stmt->close();

    } 
    $mysqli->close();