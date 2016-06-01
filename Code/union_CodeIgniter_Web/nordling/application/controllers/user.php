<?php  
header("Content-Type:text/html; charset=utf-8");
if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class User extends CI_Controller {

  public function index()
  { 
   $this->load->view('view_page1');
  }
  public function test1()
  {
    $input = $this->input->post(NULL,TRUE);

   if(empty($input['search'])){
    $name= shell_exec("python /home/z7724581/public_html/nordling/python/pdf_name.py");
    $all['name'] =$name;

    $key_arr=array_keys($input);
    $all['check']=$input;

    $pa="";
    if(in_array("abstract", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/abstract.py & ";
    }
    if(in_array("introduction", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/introduction.py & ";
    }
    if(in_array("method", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/method.py & ";
    }
    if(in_array("result", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/result.py & ";
    }
    if(in_array("discussion", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/discussion.py";
    }
    if(in_array("reference", $key_arr)){
       $pa .="python /home/z7724581/public_html/nordling/python/reference.py";   
    }
  shell_exec($pa);
  $this->load->view('view_page2',$all);
  }else{

      $input['search']=str_replace(" ","__",ltrim(rtrim($input['search'])));
      // print_r(expression)
      $name= shell_exec("python /home/z7724581/public_html/nordling/python/pdf_name.py");
      $name=str_replace("[", "", $name);
      $name=str_replace("'", "", $name);
      $name=str_replace("]", "", $name);
      $ex_name=explode(",", $name);
      
      $line ="";
      for($i=0;$i<count($ex_name);$i++){

          $ex_name[$i] = str_replace(" ","__",ltrim(rtrim($ex_name[$i])));
          $line .="python /home/z7724581/public_html/nordling/python/search.py ".$ex_name[$i]." ".$input['search'] . " & ";
      }
     shell_exec($line);
  }
  
}


  public function mysql()
  {   
    $input = $this->input->post(NULL,TRUE);
    
    /* sql choise*/
    $sent_sql['sql']=[];
    if(!empty($input['new_ribo_H_vs_N_Gene_Level'])){

        array_push($sent_sql['sql'], 'new_ribo_H_vs_N_Gene_Level');
    }
    $sent_sql['rand'] = rand(1,100000);
    
    /* method choise*/
    if($input['radio'] == 'radio1'){
       
       $sent_sql['method']        = 'Fold_change';
       $sent_sql['method_math']   = $input['select1'];
       $sent_sql['method_number'] = $input['text1'];
    }elseif($input['radio'] == 'radio2') {

       $sent_sql['method']        = 'P_Value'; 
       $sent_sql['method_math']   = '<=';
       $sent_sql['method_number'] = pow(10,$input['text2']);
    }

    $result['data']=$this->sql->gene_level($sent_sql);
    $this->load->view('view_page2',$result);
  }
  
  public function gene_img_ribo($sql_gene="",$sql_isoform="",$id="")
  {
    $ribo['data']         =$this->sql->gene_level_ribo_data($id);
    $ribo['rand']         =rand(1,10000);

    $input_h1['rand'] =$ribo['rand'];
    $input_h2['rand'] =$ribo['rand'];
    $input_n1['rand'] =$ribo['rand'];
    $input_n2['rand'] =$ribo['rand'];

    $input_h1['id_max_x'] =$ribo['data']['Max_x_h1'];
    $input_h2['id_max_x'] =$ribo['data']['Max_x_h2'];
    $input_n1['id_max_x'] =$ribo['data']['Max_x_n1'];
    $input_n2['id_max_x'] =$ribo['data']['Max_x_n2'];
    

    // echo "<pre>";
    //     print_r($ribo);
    for($i=0;$i<count($ribo['data'])-4;$i++){  
        
        $input_h1['id_max_y'] =$ribo['data'][$i]['Max_y'];
      
        $input_h1['isoform']    =$ribo['data'][$i]['Isoform'];
        $input_h1['gene']       =$ribo['data'][$i]['Gene'];
        $input_h1['length']     =$ribo['data'][$i]['Length'];
        $input_h1['cut']        =$ribo['data'][$i]['Cut'];
        $input_h1['data']       =$ribo['data'][$i]['Data_h1'];
        $input_h1['name']       ='ribo_h1';

        $this->draw_image->gene_level2($input_h1); //不同ID 相同資料庫
        
        $input_h2['id_max_y']   =$ribo['data'][$i]['Max_y'];
        $input_h2['isoform']    =$ribo['data'][$i]['Isoform'];
        $input_h2['gene']       =$ribo['data'][$i]['Gene'];
        $input_h2['length']     =$ribo['data'][$i]['Length'];
        $input_h2['cut']        =$ribo['data'][$i]['Cut'];
        $input_h2['data']       =$ribo['data'][$i]['Data_h2'];
        $input_h2['name']       ='ribo_h2';

        $this->draw_image->gene_level2($input_h2);
        
        $input_n1['id_max_y']   =$ribo['data'][$i]['Max_y'];
        $input_n1['isoform']    =$ribo['data'][$i]['Isoform'];
        $input_n1['gene']       =$ribo['data'][$i]['Gene'];
        $input_n1['length']     =$ribo['data'][$i]['Length'];
        $input_n1['cut']        =$ribo['data'][$i]['Cut'];
        $input_n1['data']       =$ribo['data'][$i]['Data_n1'];
        $input_n1['name']       ='ribo_n1';
 
        $this->draw_image->gene_level2($input_n1);
        
        $input_n2['id_max_y']   =$ribo['data'][$i]['Max_y'];
        $input_n2['isoform']    =$ribo['data'][$i]['Isoform'];
        $input_n2['gene']       =$ribo['data'][$i]['Gene'];
        $input_n2['length']     =$ribo['data'][$i]['Length'];
        $input_n2['cut']        =$ribo['data'][$i]['Cut'];
        $input_n2['data']       =$ribo['data'][$i]['Data_n2'];
        $input_n2['name']       ='ribo_n2';
        
        $this->draw_image->gene_level2($input_n2);
    }
    
    $ribo_express=$this->sql->ribo_express($id);
    $ribo['express'] = $ribo_express;
    // echo "<pre>";
    // print_r($ribo);
    $this->load->view('view_page4_gene',$ribo);
  }
  
}
?>