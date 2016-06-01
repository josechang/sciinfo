<?php 

class draw_image_0_small extends CI_Model{

    public function draw_img($data){  

       // echo "<pre>";
       // print_r($data);

       $len   = explode('..',$data['len']);
       $cut   = explode('..',$data['cut']);
       $max_cut_x   =$data['max_cut_x'];
       $data_num  = explode(',' ,$data['data']);
       $jpg   = '/home/z7724581/public_html/GD/gd_img/small'.$data['jpg'];
       
       $max_x = $data['max_x'];
     
       $max_y = $data['max_y'];

       $x    =1400;
       $y    =140;
       $img  = imagecreate($x,$y);

       $background   = imagecolorallocate($img,   245,   245, 248);

       //color
       $black     =imagecolorallocate($img,    0,   0,   0);                  
       $red       = imagecolorallocate($img, 255,   0,   0);
       $blue      = imagecolorallocate($img,   0,   0, 255);
       $green     = imagecolorallocate($img,   20,   240, 31);
       $yellow     = imagecolorallocate($img,   149,   158, 20);
       $red_black = imagecolorallocate($img,   92,   4, 4);  

       //X Y 軸
       imagefilledrectangle($img,63, 10 , 64 ,90, $black);
       imagefilledrectangle($img,64, 90 , 1385 ,91, $black);
       imagefilledrectangle($img, 65, 95,(($cut[0]/$max_cut_x)*1300)+85, 105, $red);
       imagefilledrectangle($img, (($cut[0]/$max_cut_x)*1300)+85, 95,(($cut[1]/$max_cut_x)*1300)+85 , 105, $blue);
       

       imagejpeg($img,$jpg);

    }
}

?>