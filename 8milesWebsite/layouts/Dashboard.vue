<template >
  <div id="app1">
    <!--------------- LINK --------------->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> -->
   <script src='https://kit.fontawesome.com/a076d05399.js'></script>
    <!--------------- PAGE LOADER --------------->
    <div id="preloader">
      <div class="spinner">
        <h4 class="text-muted">8 MILES TRAVEL CORP.</h4>
        <div class="bounce1"></div>
        <div class="bounce2"></div>
        <div class="bounce3"></div>
      </div>
    </div>

    <!--------------- SIDEBAR --------------->
   <div id="sidebar" >
         <div class="">
             <button @click="btn_sidebar" id="btn-close-sidebar"><i class="material-icons mi-clear" >clear</i> </button>
                                    <img src="../assets/img/liza.png" class="img-fluid sidebar-img-circle" alt="">
                                
                        <div class="sidebar-content-hide" id="sidebar-content">
                            
                               <div class="ml-3" style="border:1px solid white; height:20em; width:90%; background-color:white; border-radius:4px; box-shadow: 2px 0px 3px 0px rgb(24, 23, 23);">
                                    <div class="text-center mt-5" style="color:#929292; width:100%; font-size:1em;">Member Login</div>
                                      <div class="text-center mt-3" style="width:100%; ">
                                            <input  class="text-center" name="txtterminalid" type="text" width="30em" placeholder="Terminal / Alias">
                                      </div>
                                       <div class="text-center mt-3" style="width:100%;">
                                            <input class="text-center" name="txtuserid" type="text" width="30em" placeholder="User ID">
                                      </div>
                                      <div class="text-center mt-3" style="width:100%;">
                                            <input class="text-center" name="txtpword" type="text" width="30em" placeholder="Password">
                                      </div>
                                          <div class="text-center mt-3" style="width:100%;">
                                            <button @click="btnlogin" style="width:10em; font-color:0.5em; height:2em; background-color:#3b5998; border:0px solid red; border-radius:4px; color:white">SIGN IN</button>
                                      </div>
                                       <div class=" mt-3" style="width:100%; color:#e9a14d; margin-top:3.2em !important; ">
                                         <a class="pl-2" href="" style="font-size:12px !important; float:left;">Forgot Password?</a> 
                                         <a v-b-modal.modal-register class="pr-2"  style=" font-size:12px !important; float:right !important; color:red !important;">New User?</a>  
                                      </div>
                               </div>
             <!--------------- SOCIAL MEDIA --------------->
                                <div>
                                    <div class="text-white  mt-5 text-center " style="height:1.5em; width:100%; ">Connect Us Here!</div>
                                       
                                                <div class="row mt-3" style="width:100%; height:3em; margin:auto; padding-left:4em; padding-right:4em;">
                                                            <div class="col-sm-4  text-center">
                                                               <i class="fab fa-facebook-f social-icon-fb-main"></i>
                                                            </div>
                                                            <div class="col-lg-4 text-center">
                                                          <i class="fab fa-instagram social-icon-instagram-main"></i>
                                                            </div>
                                                            <div class="col-sm-4 text-center">
                                                                    <i class="fab fa-youtube social-icon-youtube-main"></i>
                                                            </div>
                                                   </div>
                                </div>    
                </div>
         </div>
      </div>
    <!--------------- HEADER DETAIL  --------------->
    <!-- <div id="Header-Detail">
      <div class="Header-Detail-content-left pt-2 pl-2 ">
       
      </div>
      <div class="Header-Detail-content-right pt-2 pr-1 digital-clock">
        TERMINAL ID :
      
      </div>
    </div> -->
    <!--------------- HEADER NAV --------------->
    <b-navbar
      toggleable="lg"
      type="dark"
      variant="white"
      id="Header-content"
      class="Header-content"
    >
     <button class @click="btn_sidebar" id="btn-sidebar" style="display:none;">
        <i class="material-icons social-icon-login" style="cursor:pointer; font-size:.8em;">person</i> LOGIN
      </button>
    <div class="container" >
        <!-- <a href="#" @click="index" class="navbar_logo"><img src="../assets/img/nav_logo.png" width="100px"></a> -->
        <b-navbar-brand >
            <img src="../assets/img/8Miles_Travel_Corp.png" class="img-fluid img-leftlogo"  alt />
        </b-navbar-brand>
        <b-navbar-toggle id="btntoggler" target="nav-collapse" style="background-color:#e8eef3; "></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav style="margin-right:8em;">
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto mr-5" >
              <div id="navbartabs" style="margin-top:0.5em;">
                  <b-navbar-brand class="linavbar" id="HOME" value="Flight" href="#app1">HOME</b-navbar-brand>
                  <b-navbar-brand class="linavbar" id="DESTINATION" value="Ferries" href="#div_destination">DESTINATION</b-navbar-brand>
                  <b-navbar-brand class="linavbar" id="PARTNERS" href="#div_partners">PARTNERS</b-navbar-brand>
                  <b-navbar-brand class="linavbar" id="SERVICES" href="#div_servicesoffered">SERVICES</b-navbar-brand>
                  <b-navbar-brand class="linavbar" id="PROMO" href="#div_promo">PROMO</b-navbar-brand>
                    <b-navbar-brand class="linavbar" id="ABOUT" href="#div_aboutus">ABOUT</b-navbar-brand>
                    <b-navbar-brand class="linavbar" id="CONTACT" href="#div_getintouch">CONTACT</b-navbar-brand>
                </div>
                 <b-nav-item-dropdown  style="border:0px solid red;" toggle-class="text-success Name" right>
                        <b-dropdown-item>Settings</b-dropdown-item>  
                        <b-dropdown-item  v-b-modal.modal-login >Logout</b-dropdown-item>
                      </b-nav-item-dropdown>
            </b-navbar-nav>
            </b-collapse>
         </div>
    </b-navbar>
    <div class="parallax">

    </div>
            <h2 id="div_destination" class="font-weight-light text-black container mt-5">Top Destinations</h2>
            <p class="color-black-opacity-5 container mt-2">Choose Your Next Destination</p>
                  <div  class="row mt-5  container" style="width:100%;   ">
                      <gallery :images="images_topdestination" :index="index" @close="index = null"></gallery>
                            <div class="image col-sm-3"
                            v-for="(image, imageIndex) in images_topdestination"
                            :key="imageIndex"
                            @click="index = imageIndex"
                          :style="{ backgroundImage: 'url(' + image + ')', width: '350px', height: '250px' }">
                          </div>
                </div>


  <!--------------- PARTNERS --------------->
                <div id="div_partners" class="bg-white" style=" width:100%; margin-top:5em;">
                  
                    <h2 class="font-weight-hard text-black container mt-5">PARTNERS</h2>
                      <div id="div_img_partners" class="row container" style="width:90%; ">
                      </div>
                      <div style="height:5em;"></div>
                </div>
  <!--------------- SERVICES OFFERED --------------->

 <div id="div_servicesoffered"  style=" width:100%; ">
                    <h2 class="font-weight-hard-servicesoffered text-black container " style="color:#0b464c !important;">SERVICES OFFERED</h2>
                     <div class="row container mt-5" style="width:80%;">
                        <div class="col-sm-4">
                         <h3 class="custom-text">Reservations</h3>
                         <p style="font-size: 13px;" class="">Airline Ticketing (Domestic &amp; International). Shipping Lines Ticketing. Hotel Reservation. Car Reservations</p>
                        </div>
                        <div class="col-lg-4">
                         <h3 class="custom-text">Tour Packages</h3>
                        <p style="font-size: 13px;" class="">City Tours. Adventure Tours. Aquatic Tours. Educational Tours. Group Tours/ Cruise Tours. Land Arrangement</p>
                        </div>
                        <div class="col-sm-4">
                           <h3 class="custom-text">Documentation</h3>
                          <p style="font-size: 13px;" class="">Online Passport Reservation, Red Ribbon, NSO Online Application. Tourist Visa Application</p>
                        </div>
                    </div>
                    <div class="row container mt-4" style="width:80%;">
                        <div class="col-sm-3">
                          <img src="../assets/img/Services Offered/1.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                           <p style="font-size: 13px;" class="">Domestic International Ticket Issuance</p>
                        </div>
                        <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/2.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                             <p style="font-size: 13px;" class="">Accomodation</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/3.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                            <p style="font-size: 13px;" class="">International Tour Packages</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/4.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                             <p style="font-size: 13px;" class="">Local Tour Packages</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/5.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                            <p style="font-size: 13px;" class="">Visa Assistance</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/6.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                            <p style="font-size: 13px;" class="">Car Rentals</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/7.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                            <p style="font-size: 13px;" class="">Shipping Ticket Issuance</p>
                        </div>
                           <div class="col-lg-3">
                            <img src="../assets/img/Services Offered/8.jpg" alt="" class="img-fluid" style="height:125px; width: 125px; background-color: #bbb;border-radius: 50%; display: inline-block;">
                            <p style="font-size: 13px;" class="">Travel Insurance</p>
                        </div>
                       
                    </div>
                     <div class="row container mt-4" style="width:90%;">
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/1.png" alt="" class="img-fluid" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/2.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/3.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/4.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/5.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/6.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/7.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/8.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                        <div class="col-lg-1.5">
                          <img src="../assets/img/Services Offered/9.png" alt="" class="img-fluid ml-2" style="border-radius: 50%; border: 1px solid #a1cd45; height: 90px; width: 95px;">
                        </div>
                         
                    </div>
                </div>
     <!--------------- ABOUT US --------------->
                <div id="div_aboutus" class="bg-white" style=" width:100%; margin-top:5em;">
                    <h2 class="font-weight-hard text-black container mt-5">About Us</h2>
                    <div class="container" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;">
                           Who are We
                           </div>
                    </div>
                      <div class="container mt-2" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;">
                           8-Miles Travel Corp is newly formed travel company, duly-organized and registered corporation with the Securities & Exchange Commission (SEC) on May 16, 2019 with Registration No. CS20196195 to serve the growing needs of travel and hospitality industry in the Philippines with the goal to provide travelers, their passion to explore our local tourist destination in the Philippines and abroad.
                           </div>
                    </div>
                         <div class="container mt-4" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;">
                          Mission
                           </div>
                    </div>
                      <div class="container mt-2" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;">
                           To serve our clients with enchanced travel experience by providing quality services that address their travel needs, through the most efficient arrangements so that customer loyalty, superior financial results and excellent customer satisfaction can be achieved.
                           </div>
                    </div>
                     <div class="container mt-4" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 16px; text-align:left !important;text-decoration: underline; text-decoration-color: #a1cd45;">
                          Vission
                           </div>
                    </div>
                      <div class="container mt-2" style="width:80%; ">
                         <div class=""  style="border:0px solid red; width:100%; font-size: 15px; color:#888; text-align:left !important;">
                           To be one of the most trusted and respected travel company recognized by our clients for delivering excellence. To become the leading provider of travel solutions across Philippines and to constinuously create new opportunities for growth in our strategic business.
                           </div>
                    </div>
                     
                      <div style="height:5em;"></div>
                </div>
   <!--------------- GET IN TOUCH --------------->
                <div id="div_getintouch" class="" style=" width:100%; ">
                    <h2 class="font-weight-hard-servicesoffered text-black container">Get In Touch</h2>
                      <div class="container">

                     
                            <div class="row  mt-4" style="width:90%;">
                              <div class="col-lg-6">
                                <div class="bg-white pl-3 pt-3 pb-3 container" style="heigth:5em;   ">
                                      <div class="mapouter"><div class="gmap_canvas"><iframe width="600" height="500" id="gmap_canvas" src="https://maps.google.com/maps?q=8%20miles%20travel%20corp&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                                      </div>
                                      <style>
                                      </style></div>
                                </div>
                              </div>
                              <div class="col-lg-6 ">
                                <div class="bg-white pl-3 pt-5" style="heigth:5em; width:100%; text-align:left; color:#4d4d4d;">
                                    <p class="mb-0 font-weight-bold" >Address</p>
                                    <p class="mb-4" >Rm 21 City Times Square, Basak Lapu-Lapu City, Cebu</p>
                                    <p class="mb-0 font-weight-bold mt-2" >Phone</p>
                                    <p class="mb-4" style="color:#a1cd45">236-7827 / 0917 779 2500</p>
                                      <p class="mb-0 font-weight-bold mt-2" >Email Address</p>
                                    <p class="mb-4" style="color:#a1cd45">8milestravel@gmail.com</p>
                                      <div class="" style="height:1em;">
                                     </div>
                                </div>
                              
                              </div>
                            </div>
                       </div>
                      <div style="height:5em;"></div>
                </div>
  <!--------------- PARTNERS --------------->
                <div  style=" width:100%; margin-top:5em; background-color:#333333;">
                          <div class="row container site-footer pt-5" style="width:90%;">
                          <div class="col-sm-6  " style="text-align:left;">
                                  <h3 class="footer-heading mb-4">About 8 miles Travel Corp.</h3>
                                  <p style="font-size: 13px;">
                                    8-Miles Travel Corp. is a legit Travel Company that caters all Airline ticketing (Domestic &amp; International flights), Tour Packages, Car Rental Services, Passporting, Tourist Visas etc.
                                </p>
                            </div>
                          <div class="col-lg-2 " style="text-align:left;">
                                      
                              <h3 class="footer-heading mb-4">Quick Links</h3>
                              <ul class="list-unstyled" style="font-size: 13px; color:#737373 !important;">
                                <li><a href="#"> <p>Home</p> </a></li>
                                <li><a href="#"><p>Destination</p></a></li>
                                <li><a href="#"><p>Services</p></a></li>
                                <li><a href="#"><p>About</p></a></li>
                              </ul>
                        
                          </div>
                          <div class="col-sm-2 " style="text-align:left;">
                          
                                <h3 class="footer-heading mb-4">Follow Us</h3>
                                <p>Let us be social</p>
                                <ul class="list-unstyled" style="font-size: 13px;">
                                  <li class="d-inline"><i class="fab fa-facebook social-icon-fb-footer"></i></li>
                                  <li class="d-inline ml-2"> <i class="fab fa-twitter social-icon-fb-footer"></i></li>
                                  <li class="d-inline ml-2"><i class="fab fa-instagram social-icon-fb-footer"></i></li>
                                  <li class="d-inline ml-2"> <i class="fab fa-youtube social-icon-fb-footer"></i></li>
                                </ul>
              
                          </div>
                        </div>
                      <div style="height:5em;"></div>
                </div>
<div class="container" >
  <div class="pt-3" style="height:4em; font-size:80%; font-weight:500; width:64%;">
        <a href="https://x-mediagraphicsinc.com/" target="_blank" style="color: black;"> X-Media Graphics Inc. </a>
          | MCBI-Trade Corporation | MCBI-Land Corporation | 
          <a href="https://mcbi-equipments.com/" target="_blank" style="color:black;"> MCBI-Equipments Inc. </a>
  </div>
   
</div>

    <!--------------- BODY --------------->
    <div id="Body-content">
      <!-- <nuxt /> -->
    </div>
    
    <!--------------- RETURN TO TOP --------------->
    <a id="return-to-top" @click="topfunction" class="btn btn-warning animated scroll-up-icon botfooter">
      <i id="home-icon" class="material-icons" style>local_airport</i>
    </a>
    <!--------------- FOOTER --------------->
    <div id="Footer-content">
       <div class="row" style="width:100%; height:38em; margin:auto;">
      <div class="col-sm-2" style="color:yellow; margin-top:12px; font-weight:bolder;">WELCOME USER!</div>
      <div class="col-lg-8 pt-3 text-white" style="font-size: 80%; font-weight: 400;">
          <a href="https://x-mediagraphicsinc.com/" target="_blank" style="color:white;"> X-Media Graphics Inc. </a>
          | MCBI-Trade Corporation | MCBI-Land Corporation | 
          <a href="https://mcbi-equipments.com/" target="_blank" style="color:white;"> MCBI-Equipments Inc. </a>
      </div>
      <div class="col-sm-2 pt-2" >
        <span class="badge badge-success" style="border:0px solid red; margin-left:11.9em; cursor:pointer;">Close <span class="badge badge-danger" @click="close_footer">X</span></span></div>
    </div>
    </div>
    <!--------------- RETURN TO TOP --------------->

    <!--------------- My Modal --------------->
    <div>
      <b-modal id="modal-register"  >
        <template v-slot:modal-header="{ }" >
          <b size="sm" variant="outline-none">
            <h5>Registration</h5>
          </b>
        </template>
        
         <div class="row container pt-3">
                            
                            <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for id="secORdti" style="float:left;">Flying From</label> -->
                                <input type="text" name="txt_flyingfrom" class="form-control" id="txt_flyingfrom" placeholder="AGENCY NAME" />
                              </div>
                            </div>
                            <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for id="secORdti" style="float:left;">Flying From</label> -->
                                <input type="text" name="txt_flyingfrom" class="form-control" id="txt_flyingfrom" placeholder="FULLNAME" />
                              </div>
                            </div>
                            <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for style="float:left;">Flying To</label> -->
                                <input type="text" class="form-control" name='txt_flyingto' id="txt_flyingto" placeholder="EMAIL ADDRESS" />
                              </div>
                            </div>
                           <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for style="float:left;">Flying To</label> -->
                                <input type="text" class="form-control" name='txt_flyingto' id="txt_flyingto" placeholder="MOBILE / TEL. #" />
                              </div>
                            </div>
                             <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for style="float:left;">Flying To</label> -->
                                <input type="text" class="form-control" name='txt_flyingto' id="txt_flyingto" placeholder="ADDRESS" />
                              </div>
                            </div>
                             <div class="col-md-6">
                              <div class="form-group">
                                <!-- <label for style="float:left;">Flying To</label> -->
                                <input type="text" class="form-control" name='txt_flyingto' id="txt_flyingto" placeholder="REMARKS" />
                              </div>
                            </div>
                           
                          </div>

                        


        <template
          v-slot:modal-footer="{cancel }"
        >
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button size="sm" variant="success" @click="ok()">Save</b-button>
        </template>
      </b-modal>

      <b-modal id="modal-login"  >
        <template v-slot:modal-header="{ }" >
          <b size="sm" variant="outline-none">
            <h5>Ready to Leave?</h5>
          </b>
        </template>
        
         Select "Logout" below if you are ready to end your current session.
                        


        <template
          v-slot:modal-footer="{cancel }"
        >
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button size="sm" variant="success" @click="ok()">Logout</b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>


<!-----------------   SCRIPTS  ------------------>
<script>
import axios from "axios";
import Cookies from "js-cookie";
import $ from "jquery";
import VueGallery from 'vue-gallery-slideshow';
export default {
  name: "app1",
  components: { 'gallery': VueGallery} ,
  data() {
    return {
        images_topdestination: [],
        index: null,
        Cname:null,
    };
  },
  methods: {
    logintoggle()
    {
      var uname = $('#txt_uname').val();
      if(uname == "")
      {
           document.getElementById("LOGIN").classList.toggle("linavbar_login");
          document.getElementById("navbartabs").classList.toggle("navbartabs");
          document.getElementById("navbartabsuname").classList.toggle("navbartabsinputs");
          document.getElementById("navbartabspword").classList.toggle("navbartabsinputs");
      }
      else
      {
        this.$router.push("Dash");
            
      }
        // $("#LOGIN").toggle("linavbar_login");
       
          
         
    },
    btnlogin()
    {
      alert('login');
    },
    SampleJsonData(){
       this.$router.push("SampleJsonData");
    },
    close_footer(){
      document.getElementById("Footer-content").style.display = "none";
        document.getElementById("return-to-top").classList.remove("botfooter");
    },
    // index() {
    //   this.$router.push("/");
    // },
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
   
            var Uname = Cookies.get("Uname");
            
            if (typeof Uname === "undefined") 
            {
              this.$router.push("/");
            }
         
            $(".Name").text(Cookies.get("Uname"));
      //       this.Cname = $("#Name").text();
            // alert(this.Cname);
            // -------------------- Top Destination ------------------------
             axios
      .get('https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json')
          .then(response => {
           for(var z = 0; z < response.data.RECORDS.length; z++)
                {
                  var test = {};
                  test.id = response.data.RECORDS[z].id
                  var imageLink = require('../assets/img/TopDestination/' + test.id +'.jpg');
                  var imgEL = '<img src="' + imageLink + '" class="img-fluid">'
                   this.images_topdestination.push(imageLink)
                }
            })
            // -------------------- Partners ------------------------
          axios
        .get('https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json')
            .then(response => {
            for(var z = 0; z < response.data.RECORDS.length; z++)
                  {
                    var test = {};
                    test.id = response.data.RECORDS[z].id
                    if(test.id == "1")
                      {
                          var imageLink = require('../assets/img/Partners/' + test.id +'.png');
                          var imgEL = '<a class=" col-sm-2  " href="https://mcbi-equipments.com/" target="_blank"> <img src="' + imageLink + '" class="img-fluid   imagepartners" title="MCBI EQUIPMENT"  > </a>'
                          $('#div_img_partners').append(imgEL);
                      }
                    else if(test.id == "2")
                      {
                          var imageLink = require('../assets/img/Partners/' + test.id +'.png');
                          var imgEL = '<a class=" col-sm-2  " > <img src="' + imageLink + '" class="img-fluid   imagepartners" title="MCBI TRADE CORPORATION"  > </a>'
                          $('#div_img_partners').append(imgEL);
                      }
                     else if(test.id == "3")
                      {
                          var imageLink = require('../assets/img/Partners/' + test.id +'.png');
                          var imgEL = '<a class=" col-sm-2  " > <img src="' + imageLink + '" class="img-fluid   imagepartners" title="MCBI LAND CORPORATION"  > </a>'
                          $('#div_img_partners').append(imgEL);
                      }
                     else if(test.id == "4")
                      {
                          var imageLink = require('../assets/img/Partners/' + test.id +'.png');
                          var imgEL = '<a class=" col-sm-2  " href="https://x-mediagraphicsinc.com/" target="_blank"> <img src="' + imageLink + '" class="img-fluid   imagepartners" title="X-MEDIA GRAPHICS INC."  > </a>'
                          $('#div_img_partners').append(imgEL);
                      }
                      else
                      {
                         var imageLink = require('../assets/img/Partners/' + test.id +'.png');
                          var imgEL = '<img src="' + imageLink + '" class="img-fluid col-sm-2  imagepartners" >'
                          $('#div_img_partners').append(imgEL);
                      }
                    
                    
                  }
              })




                  $('#HOME').addClass("liactive");
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

                  // var lcookie = Cookies.get("Login_terminalID");
                  // if (typeof lcookie === "undefined") {
                  //   this.$router.push("/");
                  // }

                  // $("#lbl_terminalID").text(Cookies.get("Login_terminalID"));
                  // $("#lbl_userID").text(Cookies.get("Login_userID"));

                  setTimeout(function() {
                    document.getElementById("preloader").style.opacity = 0.2;
                  }, 1990);
                  setTimeout(function() {
                    document.getElementById("preloader").style.display = "none";
                  }, 2000);

                  this.$nextTick(function() 
                  {
                      window.addEventListener("scroll", function() 
                      {
                        if (document.documentElement.scrollTop > 0) 
                          {
                             $(".linavbar").removeClass("liactive");
                             document.getElementById("HOME").classList.add("liactive");
                          }
                          if (document.documentElement.scrollTop > 600) 
                          {
                               $(".linavbar").removeClass("liactive");
                              document.getElementById("DESTINATION").classList.add("liactive");
                              
                          }
                          if (document.documentElement.scrollTop > 1200) 
                          {
                              $(".linavbar").removeClass("liactive");
                            document.getElementById("PARTNERS").classList.add("liactive");
                          }
                           if (document.documentElement.scrollTop > 1700) 
                          {
                              $(".linavbar").removeClass("liactive");
                            document.getElementById("SERVICES").classList.add("liactive");
                            
                          }
                            if (document.documentElement.scrollTop > 2500) 
                          {
                             $(".linavbar").removeClass("liactive");
                            document.getElementById("ABOUT").classList.add("liactive");
                             
                          }
                         if (document.documentElement.scrollTop > 3000) 
                          {
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
                          
                        } else {
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



<style >
.linavbar_login{
  width:29em !important;
  /* border-bottom: 1px solid #888 !important; */
 
   display:block !important;
    transition: all ease 1s;
}
.navbartabs{
  display:none;
   transition: all ease 1s;
}
.navbartabsinputs{
    display:block !important;
     transition: all ease 1s;
}
.parallax {
    background-image: url("../assets/img/headerimg.png");
    min-height: 700px;
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    
}






.btn-secondary {
    color: black; 
    background-color:white;
     border-color: white;
}
.btn-secondary:hover {
    color: black; 
    background-color:white;
     border-color: white;
}
.btn-secondary.dropdown-toggle {
    color: black !important;
    background-color: white !important;
    border-color: white !important;
}







.container{
   min-height: 0vh !important;
}
/*-----------------  HEADER DETAIL -----------------*/
#Header-Detail {
  /* text-shadow: 2px 2px rgb(90, 120, 158); */
  height: 2em;
  width: 100%;
  background-color: #435b71;
  margin: auto;
}
.Header-Detail-content-left {
  float: left;
  color: #e8eef3;
  font-size: 14px;
}
.Header-Detail-content-right {
  float: right;
  color: #e8eef3;
  font-size: 14px;
  border: 0px solid red;
  width: 27em;
  height: 2.2em;
  text-align: right;
}
/*-----------------  HEADER NAV -----------------*/
.img-leftlogo{
    width: 10em;
    margin-left:5em;
}
.liactive {
 color: #a1cd45 !important;
}
.navbar-brand {
  margin-right: 0 !important;
}
.navbar {
  padding: 0 !important;
}
.navbar_logo {
  width: 80px;
  height: 80px;
  margin-left: -40px;
  top: 13px;
  z-index: 50;
  display: block;
  position: absolute;
  left: 48%;
}

#Header-content {
  box-shadow: 0px 0px 12px 0px rgb(24, 23, 23);
  background-color: #ffffff !important;
  height:6em;
}
.Header-content {
  box-shadow: 5px 5px 5px 5px rgb(24, 23, 23);
  background-color: #ffffff !important;
}
.btnlogout {
  background-color: #d9534f;
  color: white !important;
  font-weight: bolder;

  padding-top: 0.6em;
  width: 5em;
  text-align: center;
}
.btnlogout:hover {
  background-color: #d16e6a !important;
  cursor: pointer;
}
.navbar-dark .navbar-brand {
    color: #222222;
}
.linavbar {
  height: 2.1em;
  display: inline-block;
  border: 0px solid #f0eff0;
  padding-top: 0.6em;
  width: 6.5em;
  text-align: center;
  font:  12px"Poppins", sans-serif;
}

.linavbarlogins{
   height: 2.1em;
  display: inline-block;
  border: 0px solid #f0eff0;
  padding-top: 0.6em;
  width: 0em;
  text-align: center;
  font:  12px"Poppins", sans-serif;
}
.linavbar:hover {
  color: #a1cd45 !important;
  cursor: pointer;
}
html {
  scroll-behavior: smooth !important;
}

.sticky-top {
  position: fixed;
  height: 4em !important;
  width: 100%;
  top: -70px;
  left: 0;
  right: 0;
  background: #fff;
  -webkit-transform: translateY(70px);
  -ms-transform: translateY(70px);
  transform: translateY(70px);
  -webkit-transition: background 1500ms ease, -webkit-transform 1500ms ease;
  transition: background 1500ms ease, -webkit-transform 1500ms ease;
  -o-transition: transform 1500ms ease, background 1500ms ease;
  transition: transform 1500ms ease, background 1500ms ease;
  transition: transform 1500ms ease, background 1500ms ease,
    -webkit-transform 1500ms ease;
  -webkit-transition: transform 1500ms ease, background 1500ms ease;
  -webkit-box-shadow: 0 3px 16px 0 rgba(0, 0, 0, 0.1);
  box-shadow: 0 3px 16px 0 rgba(0, 0, 0, 0.1);
}
#return-to-top {
  
  display: none;
  position: fixed;
  bottom: 10px;
  right: 10px;
  z-index: 99;
  font-size: 18px;
  cursor: pointer;
  border-width: 2px;
}
#return-to-top:hover {
  color: #d9534f;
}




.font-weight-light {
    font-weight: 300!important;
    margin-top: 2em !important;
}
.font-weight-hard {
    font-weight: 400!important;
    margin-top: 2em !important;
    padding-top: 2em;
    font-size: 1.8em;
}
.font-weight-hard-servicesoffered {
    font-weight: 400!important;
   
    padding-top: 2em;
    font-size: 1.8em;
}
.color-black-opacity-5 {
    color: rgba(0, 0, 0, 0.5);
}
.h2, h2 {
    font-size: 2.5rem;
 
}
.text-black {

    color: #000 !important;
}

/*-----------------  Body-content -----------------*/
body {
  background-color: #f8f8f8 !important;
}
#Body-content {
  height: 100%;
  border: 0px solid red;
  width: 100%;
  background-color: #f8f8f8;
  padding-top: 0em;
}
/*-----------------  Footer-content -----------------*/
.social-icon-fb-footer {
  font-size: 15px !important;
  color: #d3d7dfc5 ;
  text-shadow: 2px 2px 18px rgb(90, 120, 158);
}
.social-icon-fb-footer:hover {
  color: #ffffff;
  cursor: pointer;
}
.site-footer p {
    color: #737373;
}
.footer-heading {
    font-size: 20px;
    color: #fff;
}
.botfooter{
    margin-bottom: 2.5em;
}
#Footer-content {
  border: 0px solid red;
  height: 3em;
  width: 100%;
  text-align: center;

background-color: #268bd0;
 opacity: 0.8;
    position: fixed;
    bottom: 0px;
    right: 0px;
    z-index: 99;
    font-size: 18px;
}
/*-----------------  SideBar -----------------*/
.sidebarscroll{
margin-top:3.5em;
}
#sidebar {
  position: fixed;
  left: 0px;
  z-index: 99;
  font-size: 18px;
  cursor: pointer;
  border: 0px solid 32383d;
  background-color: #e9a14d;
  height: 100%;
  width: 0em;
  color: white;
  transition: all 1s ease;
  box-shadow: 7px 0px 7px 0px rgb(24, 23, 23);
}
.sidebar-expand {
  position: fixed;
  left: 0px;
  z-index: 99;
  font-size: 18px;
  cursor: pointer;
  border: 0px solid 32383d;
  background-color: #32383d;
  height: 100%;
  width: 20em !important;
  color: white;
  transition: all 0.5s ease;
}
#btn-sidebar {
  float: left;
  height: 4.6em;
  border: 0px solid red;
  background-color: #ffffff;
  cursor: pointer;
  width: 6.5em;
  font-size:1.3em;
  font-weight: 200;
}
.btn-sidebarscroll {
  float: left;
  height: 3.1em !important;
  border: 0px solid red;
  background-color: #ffffff;
  cursor: pointer;
  width: 4.8em;
}
#btn-sidebar:hover {
  cursor: pointer;
  background-color: #f2f2f2;
}
#btn-close-sidebar {
  float: right;
  border: 0px solid red;
  margin-top: 1em;
  margin-right: 1em;
  color: #00dbff;
  background-color: transparent;
}
#btn-close-sidebar:hover {
  color: red;
  background-color: rgba(17, 16, 16, 0.171);
}
.mi-clear {
  font-size: 55px !important;
}
.sidebar-img-circle {
  height: 100px;
  width: 100px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  border: 0px solid rgb(155, 153, 153);
  margin-left: 35.5%;
  margin-top: 12%;
  transition: all 1s ease;
}
.sidebar-img-bg {
  background-image: url("../assets/img/topimg.jpg");
  height: 15em;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-position: center;
}

.sidenav {
  margin-top: 5.5em;
  border: 0px solid red;
}
.sidenav > li {
  height: 3em;
  display: block;
  text-align: center;
  width: 100%;
  border-bottom: 1px solid #626a74;
  padding-top: 1em;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
}
.sidenav > li:hover {
  background-color: #f2f2f2;
  cursor: pointer;
  color: black;
}
.Navbarleft-home {
  display: block !important;
  transition: all 5s ease;
}
.Navbarleft-home > ul > li {
  display: block !important;
}
.Navbarleft-home > ul > li:hover {
  background-color: red;
  cursor: pointer;
}
.sidebar-content-hide {
  display: none;
}
.sidebar-content-show {
  display: inline !important;
  opacity: 1;
  visibility: visible;
}
.social-icon-youtube-main {
  font-size: 32px !important;
  color: #bd081c;
  text-shadow: 2px 2px 15px rgb(90, 120, 158);
}
.social-icon-youtube-main:hover {
  font-size: 32px;
  color: #ffffff;
}
.social-icon-instagram-main {
  font-size: 32px !important;
  color: #020202;
  text-shadow: 2px 2px 15px rgb(90, 120, 158);
}
.social-icon-instagram-main:hover {
  font-size: 32px;
  color: #ffffff;
}
.social-icon-fb-main {
  font-size: 32px !important;
  color: #3b5998 ;
  text-shadow: 2px 2px 18px rgb(90, 120, 158);
}
.social-icon-fb-main:hover {
  font-size: 32px;
  color: #ffffff;
}
.social-icon-login {
  /* font-size:52px; */
  color: #3b5998;
  text-shadow: 2px 2px 18px rgb(90, 120, 158);
}
.social-icon-login:hover {
  /* font-size:52px; */
  color: #ffffff;
}
/*-----------------  Page Loader -----------------*/
#preloader {
  position: fixed;
  left: 0;
  top: 0;
  padding-top: 15em;
  width: 100%;
  height: 100%;
  z-index: 9999;
  background: rgb(43, 41, 41);
  border: 0px solid red;
  opacity: 0.5;
}
.spinner {
  margin: 100px auto 0;
  width: 370px;
  text-align: center;
  border: 0px solid red;
}
.spinner > div {
  width: 38px;
  height: 38px;
  background-color: #fde778;
  border-radius: 100%;
  display: inline-block;
  -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  animation: sk-bouncedelay 1.4s infinite ease-in-out both;
}
.spinner .bounce1 {
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
  color: #f93;
}
.spinner .bounce2 {
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
}



/*-----------------  Top Destinations -----------------*/

.vgs__container__img {
    width: 100%;
    height: 100%;
    object-fit:fill !important;
}
.image {
    cursor: pointer;
    float: right;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    border: 1px solid #ebebeb;
    margin: 5px;
 
  }
.image:hover{
  opacity: 0.5;
}

/*-----------------  PARTNERS -----------------*/
.imagepartners {
    cursor: pointer;
    float: right;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    border: 1px solid white;
    margin: 5px;
  }
  .imagepartners:hover{
    background-color:rgba(136, 136, 136, 0.178);
  }
  /*-----------------  Service Offered -----------------*/
.custom-text {
    color: #0b464c;
    font-size: 1.3em;
}
 /*-----------------  Get in touch -----------------*/
.mapouter{position:relative;text-align:right;height:500px;width:600px;}
.gmap_canvas {overflow:hidden;background:none!important;height:500px;width:600px;}
/*-----------------   -----------------*/
@-webkit-keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
  }
}
@keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
@media only screen and (max-width: 990px) {
  .linavbar {
    width: 100%;
    text-align: left;
  }
  #btn-sidebar{
   position: absolute;
  
  }
  .img-leftlogo{
    width: 10em;
    margin-left:8em;
  }
  .navbar-toggler{
    
      height: 4.8em;
  }
  .navbar-togglerscroll{
    
      height: 3.2em !important;
  }
  .navbar-nav{
      margin-top:0em;
      background-color:white;
      width:100%;
    
  }
  .Header-content{
      padding: 2em;
  }
  
}
@media only screen and (max-width: 534px) {
  .Header-Detail-content-right {
    width: 26em;
    border: 0px solid blue;
    font-size: 12px;
  }
  .mapouter{position:relative;text-align:right;height:500px;width:400px;}
.gmap_canvas {overflow:hidden;background:none!important;height:500px;width:360px;}
}

@media (min-width: 1340px)
{
.container {
    max-width: 1540px;
  }
}
</style>