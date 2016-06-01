<?php 

class draw_image_small extends CI_Model{

    public function draw_img($data){  

       // echo "<pre>";
       // print_r($data);

       $len   = explode('..',$data['len']);
       $cut   = explode('..',$data['cut']);
       $max_cut_x   = $data['max_cut_x'];
       $data_num  = explode(',' ,$data['data']);
       $jpg   = '/home/z7724581/public_html/GD/gd_img/small'.$data['jpg'];
       
       // echo count($data_num);
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
     

       $arr2=[];

       //設定起始點
       array_push($arr2, 65);
       array_push($arr2, 89.9);

       for($i=0;$i<$cut[1];$i++){
                                             
                 array_push($arr2, ($i*1300/$max_cut_x)+85);
                      
                 if($max_y!=0){

                          array_push($arr2, 89.9-($data_num[$i]*80/$max_y));
                 }else{
                          array_push($arr2, 89.9); 
                 }                                
       }
       //設定終點

       array_push($arr2, ($cut[1]*1300/$max_cut_x)+85);// +1 是設終點  最後一點
       array_push($arr2, 89.9);

       imagefilledpolygon($img, $arr2, $cut[1]+2,$green);//+2因為頭尾是自己+的  所以陣列長度+2

       imagejpeg($img,$jpg);

    }
}

?>