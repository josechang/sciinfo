<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
 <link rel="stylesheet" href="http://140.116.215.238/~z7724581/GD1/css/auto.css" /> 
<!-- <link rel="stylesheet" href="http://140.116.215.238/~z7724581/GD1/css/reset.css" />  --> 


<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>  
<script src="http://code.jquery.com/jquery-1.11.1.js"></script>  
<script src="http://code.jquery.com/ui/1.11.0/jquery-ui.js"></script>  
<script src="http://malsup.github.io/jquery.blockUI.js"></script>

<script type="text/javascript">

            function method(num){            	                                               
                                 if(num ==1){
                                            document.getElementById('insert_textrea').style.display = "block";
                                            document.getElementById('insert_get_id').style.display  = "none";
                                            document.getElementById('field_1').value                = "";
                                            document.getElementById('field_2').value                = "";
                                            document.getElementById('field_3').value                = "";
                                            document.getElementById('new_select_1').innerHTML       = "<br><br><br>";
                                            document.getElementById('new_select_2').innerHTML       = "<br><br><br>";
                                            document.getElementById('new_select_3').innerHTML       = "<br><br><br>";
                                 }else{
                
                                             document.getElementById('insert_get_id').style.display  = "block";
                                             document.getElementById('insert_textrea').style.display = "none";
                                             document.getElementById('mytextarea').value             = "";
                                 }                       
            }

            function select_id(val){  
                                    var name=document.getElementById("field_"+val).value;

                                    $.ajax({
                                            type: 'post',
                                            url: 'http://140.116.215.238/~z7724581/GD1/index.php/user/ajax_id',
                                            data: {
                                                   get_option:val,
                                                   get_id    :name
                                            },
                                            success: function (response) {

                                                document.getElementById("new_select_"+val).innerHTML=response; 
                                            }
                                     });
                                    }

            function gd_ajax(){                      
                                 $.blockUI({ message: '<font size="8">Please Wait...</font>' });
                                 $.ajax({
                                         type: "post",
                                         url:  "http://140.116.215.238/~z7724581/GD1/index.php/user/mysql",
                                         cache: false,       
                                         data: $('#gdform').serialize(),
                                         success: function(json){            
                                                                 $('#msg').html(json); 
                                                                 $.unblockUI();                                      
                                         },
                                         error: function(){            
                                                                 alert('Error while request..');
                                                                 $.unblockUI();
                                         }
                                 });
             // $(".box").hide();
             document.getElementById("msg").style.display = "block";          
            }

            $(function() {  
            $('#field_1').autocomplete({  
                source: "http://140.116.215.238/~z7724581/GD1/php/search.php"
            });
            $('#field_2').autocomplete({  
                source: "http://140.116.215.238/~z7724581/GD1/php/search.php"
            });
            $('#field_3').autocomplete({  
                source: "http://140.116.215.238/~z7724581/GD1/php/search.php"
            });  
            }); 

            $(document).on(' change', 'input[name="select1"]', function() {
                    // alert(123);
                    $('input[name="1_ck[]"]').prop("checked", this.checked);
                });
            $(document).on(' change', 'input[name="select2"]', function() {
                    $('input[name="2_ck[]"]').prop("checked", this.checked);
                });
            $(document).on(' change', 'input[name="select3"]', function() {
                    $('input[name="3_ck[]"]').prop("checked", this.checked);
                });
  </script>

  <style type="text/css">
	   
        body{
             font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%
        }
        .top {     
                    width: 1500px;
                    height: 150px;
                    background:#7CD284;
                    margin: 0 auto;
                    padding-right: 20px;                   
        }
         #top_title {                    
                     font-weight: 700;
                     font-size: 60px;
                     color: #FFFFFF ;
                     padding-top: 30px;
                     padding-left: 25px;
                     float: left;
         }
         #top_right {                    
                     font-size: 30px;
                     color: #FFFFFF ;
                     padding-top: 100px;
                     padding-left: 30px;
                     float: right;
         }
         .box {     
               width: 1500px;
               height: 550px;                  
               margin: 0 auto;
               margin-top: 40px;
               align:center;
               position: relative;
         }
         .box_insert1 {     
                       width: 650px;                    
                       margin-left: 80px;
                       height: 500px;
                       background:#FCFDDC;
                       float: left;
                       border: black solid 3px;
         }
         .box_insert2 {     
                       width: 1500px;                  
                       margin-right: 80px;            
                       height: 500px;
                       background:#FCFDDC;
                       float: center;
                       border: black solid 3px;
         }       
         #sub1 {
                   width: 200px;
                   height: 40px;
                   margin-left:80px ;
                   margin-top: 10px;
                   border: black solid 3px;
                   background: #B5F1E9;
                   font-size: 20px;
                   font-weight: 200;
         }
         #sub2 {
                   width: 800px;
                   height: 60px;
                   margin-left:360px ;
                   margin-top: 30px;
                   border: gray solid 2px;
                   background: #E2E2F6;
                   font-size: 35px;
                   font-weight: 600;
         }
         #insert_word {
                       
                       font-weight: 700;
                       font-size: 30px;
                       color: #151875 ;
                       padding-left: 25px;
         }
         #insert_divider{                   
                         font-weight: 200;
                         font-size: 30px;
                         color: #000 ;
                         padding-left: 25px;               
         } 
         #insert_textrea{
                          margin-left:120px ;
         }
         #insert_get_id{
                          margin-left:120px ;
         }  
         #insert_checkbox{
                          font-size:27px;padding-left:200px;color:#50110A;
         }
         .bottom {     
                    width: 1520px;
                    height: 140px;
                    background:#7CD284;
                    margin: 0 auto;
                    margin-top: 60px;
                   /* align:center;*/
         }
        #msg {
               width: 1520px;
               margin: 0 auto;
               /*background:#7CD284;*/
                           
        }
      
  </style>

</head>

<body>
      <div class="top">

            <div id = 'top_title'> GD1_library </div>
            <div id = 'top_right'> Contact </div>
            <div id = 'top_right'> Help </div>
            <div id = 'top_right'> Browse </div> 
            <div id = 'top_right'> Search </div>
            <div id = 'top_right'> Home </div>

      </div>

   

      <div class="box">
            <form name="gdform" id="gdform" action="">
<!--             <div class="box_insert1"><br>
             <div id='insert_word'>請點擊查詢方式:</div>
             <input type="button" id="sub1" value="Gene" onclick="javascript:method('1');">
             <input type="button" id="sub1" value="Isoform" onclick="javascript:method('2');">  <br>
             <div id='insert_divider'>-----------------------------------------------------------</div>
       <form name="gdform" id="gdform" action="">

             <div id="insert_textrea">
                <textarea rows="9" cols="24" style="font-size:30px;" placeholder="Enter Gene Here.." name="mytextarea" id='mytextarea'></textarea>
             </div>

             <div id ='insert_get_id' style="display: none">
                  <input type="text" placeholder="Gene Symbol" id="field_1" name="mytext[]" style="font-size:25px;"       class="ui-autocomplete-input" autocomplete="off">
                  <input type="button" id="button_1" value="Get_ID" onclick="javascript:select_id(1);" style="padding-top: 5px;width:120px;height:35px;font-size:22px;"><br>
                  <div id ="new_select_1" style="width:442px; height:75px;">  </div>

                  <input type="text" placeholder="Gene Symbol" id="field_2" name="mytext[]" style="font-size:25px;"       class="ui-autocomplete-input" autocomplete="off">
                  <input type="button" id="button_2" value="Get_ID" onclick="javascript:select_id(2);" style="padding-top: 5px;width:120px;height:35px;font-size:22px;"><br>
                  <div id ="new_select_2" style="width:442px; height:75px;">  </div>

                  <input type="text" placeholder="Gene Symbol" id="field_3" name="mytext[]" style="font-size:25px;"       class="ui-autocomplete-input" autocomplete="off">
                  <input type="button" id="button_3" value="Get_ID" onclick="javascript:select_id(3);" style="padding-top: 5px;width:120px;height:35px;font-size:22px;"><br>

                  <div id ="new_select_3" style="width:442px; height:75px;">  </div>

             </div>

       </div> -->
            <div class="box_insert2"><br>

                  <div id='insert_word'>請選擇資料庫:</div><br>

                  <div id='insert_checkbox'>
                     <input type="checkbox" name="Ribo_N_vs_H" style="width: 18px; height: 18px;">Ribo_N_vs_H<br>

                  </div>

                  <div id='insert_word'>請選擇查詢方式:</div><br>
                  <div id='insert_checkbox'>
                  <form>
                     
                      <input type="radio" name="radio" value= "radio1" style="width: 18px; height: 18px;" checked/>FC                     
                      <select name="select1" style="margin-left : 60px;height: 20px;font-size: 20px;">
<!-- 　                                 <option value="case1">></option> -->
<!-- 　                                 <option value="case1"><</option> -->
                                   <option value="case1">>=</option>
                                   <option value="case2"><=</option>                       
                      </select>
                          範圍:<input type="text" name="text1" style="width: 25px; height: 20px;margin-left: 10px;font-size:20px;">
                      <br>
                      <input type="radio" name="radio" value="radio2"style="width: 18px; height: 18px;">P value

                      <select name="select2" style="margin-left : 5px;height: 20px;font-size: 20px;">
<!-- 　                                 <option value="case1">></option> -->
<!-- 　                                 <option value="case2"><</option> -->
                                   <option value="case1">>=</option>
                                   <option value="case2"><=</option>                       
                      </select>   範圍:
                      10<sup> <input type="text" name="text2" style="width: 20px; height: 10px;"></sup>
                      <br>

                  </form>
                  </div>
            </div>
           <input type="button" id="sub2" value="Search" onclick="javascript:gd_ajax();">     
        </form></div>
    
   <br><br><br><div id="msg" style="display: none"></div>
  <div class="bottom"></div>

</body>
</html>