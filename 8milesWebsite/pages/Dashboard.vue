<template>
  <div class="container text-center" style="height:150em;">
    
   
      <h6>Do you like this component?</h6>
            <h6>Custom value: {{ slider }}</h6>
            <custom-slider :values="sliderValues" raising v-model="slider"/>
            
            
            
            <h6>Default like value: {{ slider2 }}</h6>
            <div style="border:1px solid red; height:em; color">
            <label id="lblslide"  ></label></div> 
            <input id="In_slider2" v-model="slider2" placeholder="edit me">
            <custom-slider v-on:change="search" min="0" max="50" step="1" v-model="slider2"/>


  </div>
</template>

<script>
import Cookies from "js-cookie";
import $ from "jquery";
import CustomSlider from "vue-custom-range-slider";
export default {
    layout: "Dashboard",
  components: {
    CustomSlider
  },
 
  data () {
    return {
    slider: "a",
      slider2: "0",
     value:"",
      sliderValues:  
            [
                    {
                      label: "Not at all",
                      value:  "a",
                      
                    },
                    {
                      label: "A tiny bit",
                      value: "b"
                    },
                    {
                      label: "Its ok",
                      value: "c"
                    },
                    {
                      label: "Its very good",
                      value: "d"
                    },
                    {
                      label: "Its AMAZING!",
                      value: "e"
                    }
            ]  ,     
    
    }
  },
  methods: {
    search(){
            $('#lblslide').text(this.slider2 +"px")
    }
  },
  mounted () 
  {
  //     $( function() {
  //   $( "#slider-vertical" ).slider({
  //     orientation: "vertical",
  //     range: "min",
  //     min: 0,
  //     max: 100,
  //     value: 60,
  //     slide: function( event, ui ) {
  //       $( "#amount" ).val( ui.value );
  //     }
  //   });
  //   $( "#amount" ).val( $( "#slider-vertical" ).slider( "value" ) );
  // } );
        
  }
}
</script>

<style>

</style>
