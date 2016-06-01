<?php 

class science extends CI_Model{

	public function change($number){  

	if($number>0){
    
      $number=strtoupper($number);   
      if(0.0001>$number){
            
        $ex_number = explode('.',$number);
        $split     = str_split($ex_number[1]);
        if(in_array('E', $split)){

            $site  = strpos($ex_number[1], 'E'); 
            if(!empty($split[$site+3])){  
           
              $output    = $ex_number[0].".".$split[0].$split[$site].$split[$site+1].$split[$site+2].$split[$site+3]; 
            }else{

              $output    = $ex_number[0].".".$split[0].$split[$site].$split[$site+1].$split[$site+2]; 
            }
        }else{
            
            for($i=0;$i<count($split);$i++){
               if($split[$i] != 0){

                  $output    = $ex_number[0].".".$split[$i].$split[$i+1].$split[$i+2]."E-".$i;
                  break; 
               }
            }
        }
      }else{
          
        $output    = round($number,4);
      }

      }elseif($number==0){

         $output = 0; 
      }elseif($number<0){

         $number=strtoupper($number); 
         $number=substr($number,1,strlen($number));
         if(0.0001>$number){
            
            $ex_number = explode('.',$number);
            $split     = str_split($ex_number[1]);
            if(in_array('E', $split)){

              $site  = strpos($ex_number[1], 'E'); 
              if(!empty($split[$site+3])){  
           
                 $output    = "-".$ex_number[0].".".$split[0].$split[$site].$split[$site+1].$split[$site+2].$split[$site+3]; 
              }else{

                 $output    = "-".$ex_number[0].".".$split[0].$split[$site].$split[$site+1].$split[$site+2]; 
              }
            }else{
            
               for($i=0;$i<count($split);$i++){

                  if($split[$i] != 0){
 
                     $output    = "-".$ex_number[0].".".$split[$i].$split[$i+1].$split[$i+2]."E-".$i;
                     break; 
                  }
               }
            }
         }else{
          
            $output    = "-".round($number,4);
         }
      }
    return($output);
    }
}

?>