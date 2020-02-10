<template >
  <div id="app1">




    <!---------------   LINK   --------------->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>



    <!---------------   PAGE LOADER   --------------->
    <div id="preloader">
      <div class="spinner">
        <h4 class="text-muted">8 MILES TRAVEL CORP.</h4>
        <div class="bounce1"></div>
        <div class="bounce2"></div>
        <div class="bounce3"></div>
      </div>
    </div>



    <!---------------   SIDEBAR   --------------->
    <div id="sidebar" >
      <div style="border:1px solid #FFF;  height:5em;">
          <i class='fas fa-wrench ml-4 mt-4' style='font-size:40px'></i>
      </div>

      <b-button-group vertical style="width:4.5em; left:5px; " >
        <b-button @click="logo" title="LOGO">Logo</b-button>
        <b-button>Header</b-button>
        <b-button>Cover</b-button>
        <b-button>Destination</b-button>
        <b-button>Partners</b-button>
        <b-button>Services</b-button>
        <b-button>Promo</b-button>
        <b-button>Contact</b-button>
      </b-button-group>
    </div>


    
    <!---------------   NAVBAR   --------------->
    <b-navbar toggleable="lg" type="dark" variant="white" id="Header-content" class="Header-content">
      <button class @click="btn_sidebar" id="btn-sidebar" style="display:none;">
        <i class="material-icons social-icon-login" style="cursor:pointer; font-size:8em;">person</i> LOGIN
      </button>
      <div class="container">
        <b-navbar-brand>
          <!-- <img src="../assets/img/8Miles_Travel_Corp.png" class="img-fluid img-leftlogo" alt /> -->
          <img src="../assets/img/8Miles_Travel_Corp.png" id="img-resize" class="img-fluid img-leftlogo" v-bind:style="{ width: widthSize + 'em !important' }" alt />
        </b-navbar-brand>
        <b-navbar-toggle id="btntoggler" target="nav-collapse" style="background-color:#e8eef3; "></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav style="margin-right:8em;">
          <b-navbar-nav class="ml-auto mr-5">
            <div id="navbartabs"  class="mt-2">
              <b-navbar-brand class="linavbar" id="HOME" value="Flight" href="#app1">HOME</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="DESTINATION" value="Ferries" href="#div_destination">DESTINATION</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="PARTNERS" href="#div_partners">PARTNERS</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="SERVICES" href="#div_servicesoffered">SERVICES</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="PROMO" href="#div_promo">PROMO</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="ABOUT" href="#div_aboutus">ABOUT</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="CONTACT" href="#div_getintouch">CONTACT</b-navbar-brand>
            </div>
            <b-nav-item-dropdown toggle-class="text-success Name">
              <b-dropdown-item>Settings</b-dropdown-item>
              <b-dropdown-item v-b-modal.modal-login>Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>



 <!-- --------------------   Dragable Div   ------------------------ -->
 <div id="Dragable_div">
    <div id="Dragable_Logo" > 
            <div id="mydivheader">LOGO</div>
            <div class="Dragable_content">
              Resize Logo
                  <custom-slider v-on:change="search" min="0" max="50" step="1" v-model="slider2"/>
                   <!-- <label id="lblslide"  ></label> -->
                <div style="width:100%; height:1px; border-top:1px solid #888;"></div>
                  Change Logo
                  
              <input class="mt-4" style="margin-left:17%" type="file" name="pic" accept="image/*"
              onchange="document.getElementById('img-resize').src = window.URL.createObjectURL(this.files[0])">
            </div>
       </div>
 </div>



 <!----------------------   Cover Pic   ------------------------ -->
      <div class="parallax"></div>



<!-- --------------------   Top Destination   ------------------------ -->
    <div class="container text-center" >
      <h2 id="div_destination" class="font-weight-light text-black container mt-5">Top Destinations</h2>
      <p class="color-black-opacity-5 container mt-2">Choose Your Next Destination</p>
    </div>
    <div class="container text-center" >
      <div class="row mt-5 " >
        <div style=" width:80% !important">
      <no-ssr placeholder="loading...">
      <gallery :images="images_topdestination" :index="index" @close="index = null"></gallery>
      </no-ssr>
      <div class="image col-sm-3" v-for="(image, imageIndex) in images_topdestination" :key="imageIndex" @click="index = imageIndex" :style="{ backgroundImage: 'url(' + image + ')', width: '350px', height: '250px' }" ></div>
      </div>
      </div>
    </div>



    <!---------------   PARTNERS   --------------->
    <div id="div_partners" class="bg-white pb-5 mt-5" >
      <h2 class="font-weight-hard text-black  mt-5 text-center pb-2" >PARTNERS</h2>
      <div class="container">
        <div id="div_img_partners" class="row" style="margin:auto; border:0px solid red; width:60% !important"></div>
      </div>
    </div>



    <!---------------   SERVICES OFFERED   --------------->
    <div class="container text-center">
    <div class="" id="div_servicesoffered" style="width:100%; ">
      <h2 class="font-weight-hard-servicesoffered text-black container text-center" style="color:#0b464c !important;" >SERVICES OFFERED</h2>
      <div class="row container mt-5 text-center" style="width:80%; border:0px solid red; margin:auto;">
        <div class="col-sm-4">
          <h3 class="custom-text">Reservations</h3>
          <p style="font-size: 13px;">Airline Ticketing (Domestic &amp; International). Shipping Lines Ticketing. Hotel Reservation. Car Reservations</p>
        </div>
        <div class="col-lg-4">
          <h3 class="custom-text">Tour Packages</h3>
          <p style="font-size: 13px;">City Tours. Adventure Tours. Aquatic Tours. Educational Tours. Group Tours/ Cruise Tours. Land Arrangement</p>
        </div>
        <div class="col-sm-4">
          <h3 class="custom-text">Documentation</h3>
          <p style="font-size: 13px;">Online Passport Reservation, Red Ribbon, NSO Online Application. Tourist Visa Application</p>
        </div>
      </div>
      <div class="row container mt-4" style="width:80%; border:0px solid red; margin:auto;">
        <div class="col-sm-3">
          <img
            src="../assets/img/Services Offered/1.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Domestic International Ticket Issuance</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/2.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Accomodation</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/3.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>International Tour Packages</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/4.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Local Tour Packages</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/5.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Visa Assistance</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/6.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Car Rentals</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/7.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Shipping Ticket Issuance</p>
        </div>
        <div class="col-lg-3">
          <img
            src="../assets/img/Services Offered/8.jpg"
            alt
            class="img-fluid"
            style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;"
          />
          <p style="font-size: 13px;" class>Travel Insurance</p>
        </div>
      </div>
      <div class="row container mt-4" style="width:65%; border:0px solid red; margin:auto;">
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/1.png"
            alt
            class="img-fluid"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/2.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/3.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/4.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/5.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/6.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/7.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/8.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
        <div class="col-lg-1.5">
          <img
            src="../assets/img/Services Offered/9.png"
            alt
            class="img-fluid ml-2"
            style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;"
          />
        </div>
      </div>
    </div>
    </div>



    <!---------------   ABOUT US   --------------->
    <div id="div_aboutus" class="bg-white" style=" width:100%; margin-top:5em;">
      <h2 class="font-weight-hard text-black container mt-5 text-center">About Us</h2>
      <div class="container" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;"
        >Who are We</div>
      </div>
      <div class="container mt-2" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;"
        >8-Miles Travel Corp is newly formed travel company, duly-organized and registered corporation with the Securities & Exchange Commission (SEC) on May 16, 2019 with Registration No. CS20196195 to serve the growing needs of travel and hospitality industry in the Philippines with the goal to provide travelers, their passion to explore our local tourist destination in the Philippines and abroad.</div>
      </div>
      <div class="container mt-4" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;"
        >Mission</div>
      </div>
      <div class="container mt-2" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;"
        >To serve our clients with enchanced travel experience by providing quality services that address their travel needs, through the most efficient arrangements so that customer loyalty, superior financial results and excellent customer satisfaction can be achieved.</div>
      </div>
      <div class="container mt-4" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;"
        >Vission</div>
      </div>
      <div class="container mt-2" style="width:80%; ">
        <div
          class
          style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;"
        >To be one of the most trusted and respected travel company recognized by our clients for delivering excellence. To become the leading provider of travel solutions across Philippines and to constinuously create new opportunities for growth in our strategic business.</div>
      </div>
      <div style="height:5em;"></div>
    </div>



    <!---------------   GET IN TOUCH   --------------->
    <div id="div_getintouch" class style=" width:85%; margin:auto; ">
      <h2 class="font-weight-hard-servicesoffered text-black container text-center">Get In Touch</h2>
      <div class="container">
        <div class="row mt-4" style="width:100%; ">
          <div class="col-lg-6">
            <div class="bg-white  pt-3 pb-3 " >
              <div class="mapouter">
                <div class="gmap_canvas">
                 <iframe width="600" class="container" height="500" id="gmap_canvas" src="https://maps.google.com/maps?q=8%20miles%20travel%20corp&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6" style="">
            <div class="bg-white pl-3 pt-2" style="heigth:5em; width:100%; text-align:left; color:#4d4d4d;">
              <p class="mb-0 font-weight-bold">Address</p>
              <p class="mb-4">Rm 21 City Times Square, Basak Lapu-Lapu City, Cebu</p>
              <p class="mb-0 font-weight-bold mt-2">Phone</p>
              <p class="mb-4" style="color:#a1cd45">236-7827 / 0917 779 2500</p>
              <p class="mb-0 font-weight-bold mt-2">Email Address</p>
              <p class="mb-4" style="color:#a1cd45">8milestravel@gmail.com</p>
              <div class style="height:1em;"></div>
            </div>
          </div>
        </div>
      </div>
    </div>



    <!---------------   FOOTER   --------------->
    <div style="width:100%; margin-top:5em; background-color:#333333;">
          <div class="container">
          <div class="row site-footer pt-5 pb-3" style="width:80%; margin:auto; ">
            <div class="col-sm-6" style="text-align:left;">
              <h3 class="footer-heading mb-4">About 8 miles Travel Corp.</h3>
              <p style="font-size: 13px;">8-Miles Travel Corp. is a legit Travel Company that caters all Airline ticketing (Domestic &amp; International flights), Tour Packages, Car Rental Services, Passporting, Tourist Visas etc.</p>
            </div>
            <div class="col-lg-2" style="text-align:left;">
              <h3 class="footer-heading mb-4">Quick Links</h3>
              <ul class="list-unstyled" style="font-size: 13px; color:#737373 !important;">
                <li> <a href="#"> <p>Home</p> </a> </li>
                <li> <a href="#"> <p>Destination</p> </a> </li>
                <li> <a href="#"> <p>Services</p> </a> </li>
                <li> <a href="#"> <p>About</p> </a> </li>
              </ul>
            </div>
            <div class="col-sm-2 pl-5 ml-5" style="text-align:left; ">
              <h3 class="footer-heading mb-4">Follow Us</h3>
              <p>Let us be social</p>
              <ul class="list-unstyled" style="font-size: 13px;">
                <li class="d-inline">
                  <i class="fab fa-facebook social-icon-fb-footer"></i>
                </li>
                <li class="d-inline ml-2">
                  <i class="fab fa-twitter social-icon-fb-footer"></i>
                </li>
                <li class="d-inline ml-2">
                  <i class="fab fa-instagram social-icon-fb-footer"></i>
                </li>
                <li class="d-inline ml-2">
                  <i class="fab fa-youtube social-icon-fb-footer"></i>
                </li>
              </ul>
            </div>
          </div>
          </div>
    </div>
    <div class="container text-center">
      <div class="pt-3 text-center" style="height:4em; font-size:80%; font-weight:500; width:100%;">
        <a href="https://x-mediagraphicsinc.com/" target="_blank" style="color: black;">X-Media Graphics Inc.</a>| MCBI-Trade Corporation | MCBI-Land Corporation |
        <a href="https://mcbi-equipments.com/" target="_blank" style="color:black;">MCBI-Equipments Inc.</a>
      </div>
    </div>



    <!---------------   BODY   --------------->
    <div id="Body-content">
      <!-- <nuxt /> -->
    </div>



    <!---------------   RETURN TO TOP   --------------->
    <a id="return-to-top" @click="topfunction" class="btn btn-warning animated scroll-up-icon ">
      <i id="home-icon" class="material-icons" style>local_airport</i>
    </a>



    <!---------------   FOOTER POPUP   --------------->
    <div id="Footer-content" style="display:none;">
      <div class="row" style="width:100%; height:38em; margin:auto;">
        <div class="col-sm-2" style="color:yellow; margin-top:12px; font-weight:bolder;">WELCOME USER!</div>
        <div class="col-lg-8 pt-3 text-white" style="font-size: 80%; font-weight: 400;">
          <a href="https://x-mediagraphicsinc.com/" target="_blank" style="color:white;" >X-Media Graphics Inc.</a> | MCBI-Trade Corporation | MCBI-Land Corporation |
          <a href="https://mcbi-equipments.com/" target="_blank" style="color:white;">MCBI-Equipments Inc.</a>
        </div>
        <div class="col-sm-2 pt-2">
          <span class="badge badge-success" style="border:0px solid red; margin-left:11.9em; cursor:pointer;">
            Close
            <span class="badge badge-danger" @click="close_footer">X</span>
          </span>
        </div>
      </div>
    </div>



    <!---------------   My Modal   --------------->
    <div>
      <b-modal id="modal-register">
        <template v-slot:modal-header="{ }">
          <b size="sm" variant="outline-none">
            <h5>Registration</h5>
          </b>
        </template>

        <div class="row container pt-3">
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                name="txt_flyingfrom"
                class="form-control"
                id="txt_flyingfrom"
                placeholder="AGENCY NAME"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                name="txt_flyingfrom"
                class="form-control"
                id="txt_flyingfrom"
                placeholder="FULLNAME"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                name="txt_flyingto"
                id="txt_flyingto"
                placeholder="EMAIL ADDRESS"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                name="txt_flyingto"
                id="txt_flyingto"
                placeholder="MOBILE / TEL. #"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                name="txt_flyingto"
                id="txt_flyingto"
                placeholder="ADDRESS"
              />
            </div>
          </div>
          <div class="col-md-6">
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                name="txt_flyingto"
                id="txt_flyingto"
                placeholder="REMARKS"
              />
            </div>
          </div>
        </div>
        <template v-slot:modal-footer="{cancel }">
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button size="sm" variant="success" @click="ok()">Save</b-button>
        </template>
      </b-modal>
      <b-modal id="modal-login">
        <template v-slot:modal-header="{ }">
          <b size="sm" variant="outline-none">
            <h5>Ready to Leave?</h5>
          </b>
        </template>
        Select "Logout" below if you are ready to end your current session.
        <template
          v-slot:modal-footer="{cancel }">
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button size="sm" variant="success" @click="ok()">Logout</b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>



<!-----------------   STYLE   ------------------>
<style scoped src="@/assets/css/editlayout_dashboard.css">
</style>



<!-----------------   SCRIPTS   ------------------>
<script>
// require('@/assets/css/editlayout_dashboard.css')
// import "vue-custom-range-slider/dist/vue-custom-range-slider.css";
import CustomSlider from "vue-custom-range-slider";
import axios from "axios";
import Cookies from "js-cookie";
import $ from "jquery";
import VueGallery from "vue-gallery-slideshow";
export default {
  name: "app1",
  components: { gallery: VueGallery, CustomSlider },
  data() 
  {
    return {
      widthSize:5,

      images_topdestination: [],
      index: null,
      Cname: null,
      slider2: "0",
          
    };
  },
  methods: {
     search(){
            // $('#lblslide').text(this.slider2 +"px")
            this.widthSize = this.slider2;
    },
    logo()
    {
       document.getElementById("Dragable_div").classList.toggle("Dragable_Logo_show");
    },
    logintoggle() {
      var uname = $("#txt_uname").val();
      if (uname == "") {
        document.getElementById("LOGIN").classList.toggle("linavbar_login");
        document.getElementById("navbartabs").classList.toggle("navbartabs");
        document
          .getElementById("navbartabsuname")
          .classList.toggle("navbartabsinputs");
        document
          .getElementById("navbartabspword")
          .classList.toggle("navbartabsinputs");
      } else {
        this.$router.push("Dash");
      }
    },
    btnlogin() {
      alert("login");
    },
    SampleJsonData() {
      this.$router.push("SampleJsonData");
    },
    close_footer() {
      document.getElementById("Footer-content").style.display = "none";
      document.getElementById("return-to-top").classList.remove("botfooter");
    },
    btn_sidebar() {
      document.getElementById("sidebar").classList.toggle("sidebar-expand");
      setTimeout(function() {
        document
          .getElementById("sidebar-content")
          .classList.toggle("sidebar-content-show");
      }, 200);
    },
    ok() {
      Cookies.remove("Uname");
      this.$router.push("/");
    },
    PageName: function(event) {
      var page = event.target.id;
      $(".linavbar").removeClass("liactive");
      $(event.target).addClass("liactive");
      this.$router.push(page);
    },
    btnhidehome() {
      var nh = document.getElementById("Navbarleft-home");
      nh.classList.toggle("Navbarleft-home");
    },
    topfunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
  },
  mounted() {
            

              //  dragElement(document.getElementById("Dragable_Logo"));

              //                   function dragElement(elmnt) {
              //                     var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
              //                     if (document.getElementById(elmnt.id + "header")) {
                                 
              //                       document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
              //                     } else {
                                  
              //                       elmnt.onmousedown = dragMouseDown;
              //                     }

              //                     function dragMouseDown(e) {
              //                       e = e || window.event;
              //                       e.preventDefault();
                                
              //                       pos3 = e.clientX;
              //                       pos4 = e.clientY;
              //                       document.onmouseup = closeDragElement;
                                
              //                       document.onmousemove = elementDrag;
              //                     }

              //                     function elementDrag(e) {
              //                       e = e || window.event;
              //                       e.preventDefault();
                                   
              //                       pos1 = pos3 - e.clientX;
              //                       pos2 = pos4 - e.clientY;
              //                       pos3 = e.clientX;
              //                       pos4 = e.clientY;
                                
              //                       elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
              //                       elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
              //                     }

              //                     function closeDragElement() {
                                   
              //                       document.onmouseup = null;
              //                       document.onmousemove = null;
              //                     }
              //                   }



    var Uname = Cookies.get("Uname");
    if (typeof Uname === "undefined") 
    {
      this.$router.push("/");
    }
    $(".Name").text(Cookies.get("Uname"));
   



    // -------------------- Top Destination ------------------------
    axios.get(
        "https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json")
      .then(response => {
        for (var z = 0; z < 6; z++) {
          var test = {};
          test.id = response.data.RECORDS[z].id;
          var imageLink = require("../assets/img/TopDestination/" + test.id +
            ".jpg");
          var imgEL = '<img src="' + imageLink + '" class="img-fluid">';
          this.images_topdestination.push(imageLink);
        }
      });



    // -------------------- Partners ------------------------
    axios.get( "https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json" )
      .then(response => {
        for (var z = 0; z < 4; z++) 
        {
              var test = {};
              test.id = response.data.RECORDS[z].id;
              if (test.id == "1") 
              {
                var imageLink = require("../assets/img/Partners/" + test.id + ".png");
                var imgEL = '<a class="col-sm-3" style="margin-top:3em;"  href="https://mcbi-equipments.com/" target="_blank"> <img src="' + imageLink + '" class="img-fluid  imagepartners"  title="MCBI EQUIPMENT"  > </a>';
                $("#div_img_partners").append(imgEL);
              } 
              else if (test.id == "2") 
              {
                var imageLink = require("../assets/img/Partners/" + test.id + ".png");
                var imgEL = '<a class="col-sm-3" > <img src="' + imageLink + '" class="img-fluid imagepartners " title="MCBI TRADE CORPORATION"  > </a>';
                $("#div_img_partners").append(imgEL);
              } else if (test.id == "3") {
                var imageLink = require("../assets/img/Partners/" + test.id + ".png");
                var imgEL ='<a class="col-sm-3" style="margin-top:3em;" > <img src="' + imageLink + '" class="img-fluid imagepartners " style="width:20em;" title="MCBI LAND CORPORATION"  > </a>';
                $("#div_img_partners").append(imgEL);
              } 
              else if (test.id == "4") 
              {
                var imageLink = require("../assets/img/Partners/" + test.id + ".png");
                var imgEL ='<a class="col-sm-3" style="margin-top:3em;" href="https://x-mediagraphicsinc.com/" target="_blank"> <img src="' + imageLink +'" class="img-fluid imagepartners "  title="X-MEDIA GRAPHICS INC."  > </a>';
                $("#div_img_partners").append(imgEL);
              } 
              else 
              {
                var imageLink = require("../assets/img/Partners/" +test.id + ".png");
                var imgEL ='<a class="col-sm-3" style="margin-top:3em;" > <img src="' + imageLink +'" class="img-fluid imagepartners "  title="X-MEDIA GRAPHICS INC."  > </a>';
                $("#div_img_partners").append(imgEL);
              }
        }
      });



    $("#HOME").addClass("liactive");
    $(document).ready(function() {
      clockUpdate();
      setInterval(clockUpdate, 1000);
    });




    function clockUpdate() {
      var date = new Date();
      //    $('.digital-clock').css({'color': '#fff', 'text-shadow': '0 0 6px #ff0'});
      $(".digital-clock");
      function addZero(x) {
        if (x < 10) {
          return (x = "0" + x);
        } else {
          return x;
        }
      }
      function twelveHour(x) {
        if (x > 12) {
          return (x = x - 12);
        } else if (x == 0) {
          return (x = 12);
        } else {
          return x;
        }
      }
      var h = addZero(twelveHour(date.getHours()));
      var m = addZero(date.getMinutes());
      var s = addZero(date.getSeconds());
      $(".digital-clock").text("Time: " + h + ":" + m + ":" + s);
    }



    setTimeout(function() {
      document.getElementById("preloader").style.opacity = 0.2;
    }, 1990);
    setTimeout(function() {
      document.getElementById("preloader").style.display = "none";
    }, 2000);




    this.$nextTick(function() {
      window.addEventListener("scroll", function() {
        if (document.documentElement.scrollTop > 0) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("HOME").classList.add("liactive");
        }
        if (document.documentElement.scrollTop > 600) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("DESTINATION").classList.add("liactive");
        }
        if (document.documentElement.scrollTop > 1200) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("PARTNERS").classList.add("liactive");
        }
        if (document.documentElement.scrollTop > 1700) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("SERVICES").classList.add("liactive");
        }
        if (document.documentElement.scrollTop > 2500) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("ABOUT").classList.add("liactive");
        }
        if (document.documentElement.scrollTop > 3000) {
          $(".linavbar").removeClass("liactive");
          document.getElementById("CONTACT").classList.add("liactive");
        }
        var navBar = document.getElementById("Header-content");
        var btnsidebar = document.getElementById("btn-sidebar");
        var btntogglers = document.getElementById("btntoggler");
        var sidebars = document.getElementById("sidebar");
        if (document.documentElement.scrollTop > 100) {
          navBar.classList.add("sticky-top");
          document.getElementById("return-to-top").style.display = "block";
          btnsidebar.classList.add("btn-sidebarscroll");
          btntogglers.classList.add("navbar-togglerscroll");
          sidebars.classList.add("sidebarscroll");
          document.getElementById("Dragable_div").style.marginTop = "16.8em";
        } else {
            document.getElementById("Dragable_div").style.marginTop = "7.5%";
          sidebars.classList.remove("sidebarscroll");
          navBar.classList.remove("sticky-top");
          btntogglers.classList.remove("navbar-togglerscroll");
          btnsidebar.classList.remove("btn-sidebarscroll");
          document.getElementById("return-to-top").style.display = "none";
        }
      });
    });
  }
};
</script>


