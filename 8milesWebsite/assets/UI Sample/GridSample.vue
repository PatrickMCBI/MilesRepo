<template>
<!-- <no-ssr> -->
        <div id="sample">
          
            <div id="gridview">
                <div>left</div> <div>center</div> <div>right</div>
                <div id="leftside">leftside</div> <div id="main">MAIN</div> <div id="rightside">rightside</div>
            </div>
            <div id="footer">
                <div>footer</div>
            </div> 

            
        <div id="content">
                <div style="background-color:green; ">
                </div>
                <div style="background-color:yellow;">
                </div>
                <div style="background-color:red;">
                </div>
                <div style="background-color:blue;">
                </div>
            </div>

            <div style="height:50em; margin-top:5em;">
                <input type="text" id="fname" placeholder="Firstname">
                <input type="text" id="lname" placeholder="Lastname">
                <input type="button" value="Save" @click="save" >
                <br><br>
                Person Lists
                <div style=" width:50%;  margin-left:2em;">
              <table style="width:100%; " id="table">
                <tr style="border-bottom:1px solid red; height:0.1em !important; text-align:center; background-color:#4ECB4A; color:#eeeeee;">
                  <th>No.</th>
                  <th>Firstname</th>
                  <th>Lastname</th> 
                    <th>DELETE</th>
                </tr>
              </table>
            </div>
         </div>
 </div>
 <!-- </no-ssr> -->
</template>

<script>
import $ from "jquery";
export default {
  name: "sample",
  components: {},
  data(){
     return {
      lastnum:""
     }
  },
  methods:{
    save()
    {
      var res = (parseInt(this.lastnum) +1);
      var imgEL = '<tr ><td style="border:1px solid red;">'+ res +'</td><td style="border:1px solid red;">'+$('#fname').val()+'</td><td style="border:1px solid red;">'+$('#lname').val()+'</td></tr>';
     this.lastnum =res;
     $("#table").append(imgEL);
         
    },
    delete()
    {
       alert('delete');
    }
    //   delete: function(event) {
    //     alert('delete');
    //      console.log(event.target);
    // }
  },
  mounted()
  {
       for (var z = 1; z <= 5; z++) 
          {
              var imgEL = '<tr><td style="border:1px solid red;" class="num" id="">'+z+'</td><td style="border:1px solid red;">'+z+'</td><td style="border:1px solid red;">'+z+'</td><td style="border:1px solid red; text-align:center;"><input type="button" style="color:red" value="X" onclick="delete()"></td></tr></tr>'; 
              $("#table").append(imgEL);
               this.lastnum = z;
         
         } 
  }
}
</script>

<style scoped>
/* --------------- Sample 3 ------------------ */

/* --------------- Sample 2 ------------------ */
   body {
        padding: 0 !important;
        margin: 0 !important;
  
    }
    
    #content {
        font-size: 0px;
        width: 100%;
        padding: 0;
        margin: 0;
        word-spacing: 0px !important;
    }
    
    #content>div {
        width: 25%;
        height: 300px;
        display: inline-block;
        margin: 0;
       
    }


/* --------------- Sample 1 ------------------ */
#gridview
  {
    border:1px solid red;
    text-align:center;
    display:grid;
    grid-template-areas:'header header header';
    grid-template-columns: 17% auto 17%;
    grid-template-rows: 5%;
    height:40em;
    grid-gap: 10px;
  }
#gridview > div
  {
    border:1px solid red;
  }
#gridview > div > #leftside
  {
    border:1px solid red;
    display:grid;
    grid-template-areas:'header header header';
    grid-template-columns: 17% auto 17%;
  }
#footer
  {
    border:1px solid blue;
    display:grid;
    grid-template-areas:100%;
    grid-template-columns: 100%;
    text-align:center;
  }
  #footer > div
  {
    border:1px solid blue;
    grid-template-columns: 90%;
    text-align:center;
  } 
</style>