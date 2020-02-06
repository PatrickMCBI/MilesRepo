<template>
  <div class="container">
     <div class="row mt-5  container" style="width:100%;   ">
                   <div>
                    {{ info }}
                  </div>
                  <label id="lblid"></label>
                     <gallery :images="images_topdestination" :index="index" @close="index = null"></gallery>
                  <div id="div_img"></div>
                
                      <gallery :images="images_topdestination" :index="index" @close="index = null"></gallery>
                            <div  style="" class="image col-sm-3"
                            v-for="(image, imageIndex) in images_topdestination"
                            :key="imageIndex"
                            @click="index = imageIndex"
                         :style="{ backgroundImage: 'url(' + image + ')', width: '350px', height: '250px' }">
                          </div>
                    
                </div>
  </div>
</template>
 
<script>
  import VueGallery from 'vue-gallery-slideshow';
  import axios from 'axios'
  import $ from "jquery";
  export default {
   
      layout: "MainLayout",
  
   components: { 'gallery': VueGallery},
 data() {
    return {
       info: [],
        images_topdestination: [],
        index: null,
    };
    //    images_topdestination: [
    //       require('../assets/img/liza.png'),
    //       'https://8milestravel.com/images/destinations/image-2.jpg',
    //       'https://8milestravel.com/images/destinations/image-3.jpg',
    //       'https://8milestravel.com/images/destinations/image-4.jpg',
    //       'https://8milestravel.com/images/destinations/image-5.jpg',
    //       'https://8milestravel.com/images/destinations/image-6.jpg',
          
           
    //     ],
    //     index: null,
    // };
  },
  mounted () {
     axios
      .get('https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json')
          .then(response => {
            //  this.info = response.data
            // this.info = response.data
              // console.log(response.data.RECORDS); 
               for(var z = 0; z < response.data.RECORDS.length; z++)
                {
                 var test = {};
                  test.id = response.data.RECORDS[z].id
                  $("#lblid").append(test.id);
                    var imageLink = require('../assets/img/' + test.id +'.png');
                    var imgEL = '<img src="' + imageLink + '" class="img-fluid">'
                   $('#div_img').append(imgEL);
                   this.images_topdestination.push(imageLink)
                }
            })
  }
}
</script>
<style scoped>
  .image {
    cursor: pointer;
    float: left;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    border: 1px solid #ebebeb;
    margin: 5px;
  }
</style> 
 