<?php 

class draw_id extends CI_Model{

    public function draw_img($data){  

       // echo "<pre>";
       // print_r($data);

       $len   = explode('..',$data['data']['COL3']);
       $cut   = explode('..',$data['data']['COL4']);
       $data_num  = explode(',' ,$data['data']['COL5']);
       $data['jpg'] = 'one_id'.$data['rand'].$data['data']['COL1'].'_'.$data['data']['COL2']."_".$data['sql'].'.jpg';
       $jpg   = '/home/z7724581/public_html/GD1/gd_img/'.$data['jpg'];
       
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
       imagefilledrectangle($img, 65, 95,(($cut[0]/$max_x)*1300)+85, 105, $red);
       imagefilledrectangle($img, (($cut[0]/$max_x)*1300)+85, 95,(($cut[1]/$max_x)*1300)+85 , 105, $blue);
       imagefilledrectangle($img, (($cut[1]/$max_x)*1300)+85, 95,(($len[1]/$max_x)*1300)+85 , 105, $yellow);

       $font_size =10 ;//SIZE
       $rotation  =0  ;//angle
       $font      ="fonts/Amphion.ttf";//字型

       #長條圖底下素質
       $origin_y  =120;

       $origin_x  =65;
       $text    = 1;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       
       $origin_x  =(($cut[0]/$max_x)*1300)+85;
       $text      = $cut[0];
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       $origin_x  =(($cut[1]/$max_x)*1300)+85;
       $text      = $cut[1];
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       $origin_x  =(($len[1]/$max_x)*1300)+45;
       $text      = $len[1];
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       $arr2=[];

       //設定起始點
       array_push($arr2, 65);
       array_push($arr2, 89.9);

       for($i=0;$i<$len[1];$i++){
                                             
                 array_push($arr2, ($i*1300/$max_x)+85);
                      
                 if($max_y!=0){

                          array_push($arr2, 89.9-($data_num[$i]*80/$max_y));
                 }else{
                          array_push($arr2, 89.9); 
                 }                                
       }
       //設定終點

       array_push($arr2, (($len[1])*1300/$max_x)+85);// +1 是設終點  最後一點
       array_push($arr2, 89.9);

       imagefilledpolygon($img, $arr2, $len[1]+2,$green);//+2因為頭尾是自己+的  所以陣列長度+2

       //左尺刻度
       imagefilledrectangle($img,59, 10 , 60 ,90, $red_black); //垂直線
       imagefilledrectangle($img,49, 10 , 59 ,10, $red_black); //平行長的線
       imagefilledrectangle($img,51, 50 , 59 ,50, $red_black);
       imagefilledrectangle($img,49, 90 , 59 ,90, $red_black);
       imagefilledrectangle($img,54, 18 , 59 ,18, $red_black); //平行短的線
       imagefilledrectangle($img,54, 26 , 59 ,26, $red_black);
       imagefilledrectangle($img,54, 34 , 59 ,34, $red_black);
       imagefilledrectangle($img,54, 42 , 59 ,42, $red_black);
       imagefilledrectangle($img,54, 58 , 59 ,58, $red_black);
       imagefilledrectangle($img,54, 66 , 59 ,66, $red_black);
       imagefilledrectangle($img,54, 74 , 59 ,74, $red_black);
       imagefilledrectangle($img,54, 82 , 59 ,82, $red_black);

       $font_size =9 ;//SIZE
       $rotation  =0  ;//angle
       $font      ="fonts/Amphion.ttf";//字型
       $origin_x  =24;
       $origin_y  =92;
       $text      =0;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       $a=$max_y;
       if($a>0.001){

                    $origin_x=13.5;
                    $origin_y=12;
                    $a=round($a,2);

       }elseif(0.001>= $a and $a> 0.0000000001){

                    $a1=(int)(log10($a));
                    $a2=(string)(log10($a));
                    $a3=(string)(round(pow(10,((float)str_replace($a2[0].$a2[1], "-0", $a2))),1))."E".$a1;

                    $origin_x=2;
                    $origin_y=12;
                    $a=$a3;
       }elseif($a==0){

                    $origin_x=24;
                    $origin_y=12;
                    $a=0;
       }else{
                    $a1=(int)(log10($a));
                    $a2=(string)(log10($a));
                    $a3=(string)(round(pow(10,((float)str_replace($a2[0].$a2[1].$a2[2], "-0", $a2))),1))."E".$a1;

                    $font_size =8.5 ;
                    $origin_x=0;
                    $origin_y=9;
                    $a=$a3;
       }

       $text    = $a;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       imagejpeg($img,$jpg);

    }
}

?>