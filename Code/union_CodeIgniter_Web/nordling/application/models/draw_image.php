<?php 

class draw_image extends CI_Model{


  public function gene_level2($data){  

       // echo "<pre>";
       // print_r($data);   
       $isoform  = $data['isoform'];
       $gene     = $data['gene'];
       $sql      = $data['name'];
       $rand     = $data['rand'];
       $len      = explode('..',$data['length']);
       $cut      = explode('..',$data['cut']);
       $max_x    = $len[1];
       $max_y    = $data['id_max_y'];

       if($data['data'] !='No'){
          $figure  = explode(',' ,$data['data']);    
       }

       $jpg   = "/home/z7724581/public_html/GD1/gd_img/gene_level2_".$sql."_".$isoform."_".$gene."_".$rand.".jpg";
       
       $x    =1450;
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
       
       imagefilledrectangle($img, 65, 95,(($cut[0]/$max_x)*1320)+65, 105, $red);
       
     
       imagefilledrectangle($img, (($cut[0]/$max_x)*1320)+65, 95,(($cut[1]/$max_x)*1320)+65 , 105, $blue);
       imagefilledrectangle($img, (($cut[1]/$max_x)*1320)+65, 95,(($len[1]/$max_x)*1320)+65 , 105, $yellow);

       $font_size =10 ;//SIZE
       $rotation  =0  ;//angle
       $font      ="fonts/Amphion.ttf";//字型

       #長條圖底下素質
       $origin_y  =120;
       $origin_x  =65;
       $text    = 1;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       

       $origin_x  =(($cut[0]/$max_x)*1320)+65;
       
       if(($cut[0]/$max_x)<0.03){
         
           $origin_y  = 132;      
       }else{

           $origin_y  = 120; 
       }
       $text      = $cut[0];
       if($cut[0]!=1){
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       }

       $origin_x  =(($cut[1]/$max_x)*1300)+85;
       if((($cut[1]-$cut[0])/$max_x)<0.03){

           $origin_y  = 132;      
       }else{

           $origin_y  = 120; 
       }
       $text      = $cut[1];
       if($cut[0]!=1 or $cut[0]!=$cut[1]){
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       }

       $origin_x  =(($len[1]/$max_x)*1300)+85;
       if((($len[1]-$cut[1])/$max_x)<0.03){

           $origin_y  = 132;      
       }else{

           $origin_y  = 120; 
       }
       $text      = $len[1];
       if($cut[1]!=$len[1]){
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);
       }
  if($data['data'] !='No'){
       $arr2=[];
 
       for($i=0;$i<count($figure);$i++){
           
           $key_val =explode("_", $figure[$i]);  
           array_push($arr2, ($key_val[0]*1300/$max_x)+85); 
           array_push($arr2, 89.9);

           array_push($arr2, ($key_val[0]*1300/$max_x)+85);               
           if($max_y!=0){

              array_push($arr2, 89.9-($key_val[1]*80/$max_y));
           }else{

              array_push($arr2, 89.9); 
           }

           array_push($arr2, (($key_val[0]*1300)/$max_x)+85); 
           array_push($arr2, 89.9);                                
       }
       //設定終點

       array_push($arr2, (($len[1])*1300/$max_x)+85);// +1 是設終點  最後一點
       array_push($arr2, 89.9);

       imagefilledpolygon($img, $arr2, count($arr2)/2,$green);//+2因為頭尾是自己+的  所以陣列長度+2
     }
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

       $font_size =10 ;//SIZE
       $rotation  =0  ;//angle
       $font      ="fonts/Amphion.ttf";//字型

       $origin_x  =15;
       $origin_y  =9;
       $text    = $max_y;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       $origin_x  =18;
       $origin_y  =90;
       $text      =0;
       imagettftext($img, $font_size, $rotation, $origin_x, $origin_y, $black ,$font, $text);

       imagejpeg($img,$jpg);

  }
}

?>