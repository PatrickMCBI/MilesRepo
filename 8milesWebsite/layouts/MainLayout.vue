<template >
  <div id="app">
    <!--------------- LINK --------------->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
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
    <div id="sidebar">
      <div class>
        <button @click="btn_sidebar" id="btn-close-sidebar">
          <i class="material-icons mi-clear">clear</i>
        </button>
        <img src="../assets/img/liza.png" class="img-fluid sidebar-img-circle" alt />

        <div class="sidebar-content-hide" id="sidebar-content">
          <div
            class="ml-3"
            style="border:1px solid white; height:20em; width:90%; background-color:white; border-radius:4px; box-shadow: 2px 0px 3px 0px rgb(24, 23, 23);"
          >
            <div
              class="text-center mt-5"
              style="color:#929292; width:100%; font-size:1em;"
            >Member Login</div>
            <div class="text-center mt-3" style="width:100%; ">
              <input
                class="text-center"
                name="txtterminalid"
                type="text"
                width="30em"
                placeholder="Terminal / Alias"
              />
            </div>
            <div class="text-center mt-3" style="width:100%;">
              <input
                class="text-center"
                name="txtuserid"
                type="text"
                width="30em"
                placeholder="User ID"
              />
            </div>
            <div class="text-center mt-3" style="width:100%;">
              <input
                class="text-center"
                name="txtpword"
                type="text"
                width="30em"
                placeholder="Password"
              />
            </div>
            <div class="text-center mt-3" style="width:100%;">
              <button
                @click="btnlogin"
                style="width:10em; font-color:0.5em; height:2em; background-color:#3b5998; border:0px solid red; border-radius:4px; color:white"
              >SIGN IN</button>
            </div>
            <div class="mt-3" style="width:100%;  margin-top:3.2em !important;  color:blue !important;">
              <a class="pl-2" href style="font-size:12px !important; float:left; ">Forgot Password?</a>
              <a v-b-modal.modal-register class="pr-2" style=" font-size:12px !important; float:right !important;">New User?</a>
            </div>
          </div>
          <!--------------- SOCIAL MEDIA --------------->
          <div>
            <div
              class="text-white mt-5 text-center"
              style="height:1.5em; width:100%; "
            >Connect Us Here!</div>

            <div
              class="row mt-3"
              style="width:100%; height:3em; margin:auto; padding-left:4em; padding-right:4em;"
            >
              <div class="col-sm-4 text-center">
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
      <div class="container">
        <b-navbar-brand>
          <img src="../assets/img/8Miles_Travel_Corp.png" class="img-fluid img-leftlogo" alt />
        </b-navbar-brand>
        <b-navbar-toggle id="btntoggler" target="nav-collapse" style="background-color:#e8eef3; "></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav style="margin-right:8em;">
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto mr-5">
            <div id="navbartabs">
              <b-navbar-brand class="linavbar" id="HOME" value="Flight" href="#app">HOME</b-navbar-brand>
              <b-navbar-brand
                class="linavbar"
                id="DESTINATION"
                value="Ferries"
                href="#div_destination"
              >DESTINATION</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="PARTNERS" href="#div_partners">PARTNERS</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="SERVICES" href="#div_servicesoffered">SERVICES</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="PROMO" href="#div_promo">PROMO</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="ABOUT" href="#div_aboutus">ABOUT</b-navbar-brand>
              <b-navbar-brand class="linavbar" id="CONTACT" href="#div_getintouch">CONTACT</b-navbar-brand>
            </div>
            <b-navbar-brand
              class="linavbarlogins"
              id="LOGIN"
              style="color:black; transition: all ease 1s;"
            >
              <div class="row container mb-5" style="margin-top:-4px !important;">
                <div class="col-md-6" id="navbartabsuname" style="display:none;">
                  <div class style=" ">
                    <input
                      type="text"
                      tabindex="1"
                      name="txt_flyingfrom"
                      id="txt_uname"
                      placeholder="USERNAME"
                    />
                  </div>
                  <div class="text-left mt-1" style="width:130%; color:#ed302b; ">
                    <a tabindex="4" href style="color:blue; ">Forgot Password?</a>
                  </div>
                </div>
                <div class="col-md-6 pl-4" id="navbartabspword" style="display:none;">
                  <div class style>
                    <input
                      type="password"
                      tabindex="2"
                      name="txt_flyingfrom"
                      id="txt_flyingfrom"
                      placeholder="PASSWORD"
                    />
                  </div>
                  <div class="text-right mt-1" style="width:130%; ">
                    <a
                      tabindex="5"
                      href="#"
                    
                    
                    ><router-link to="/Registration"  target="_blank"   style="color:#ed302b; cursor:pointer; "> New User?</router-link></a>
                  </div>
                </div>
              </div>
            </b-navbar-brand>
            <b-navbar-brand
              class="linavbar ml-2"
              tabindex="3"
              @click="logintoggle"
              style="color:black; outline:none;"
            >LOGIN</b-navbar-brand>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <div class="parallax"></div>
    <h2 id="div_destination" class="font-weight-light text-black container mt-5">Top Destinations</h2>
    <p class="color-black-opacity-5 container mt-2">Choose Your Next Destination</p>
    <div class="row mt-5 container" style="width:100%;   ">
         <no-ssr placeholder="loading...">
      <gallery :images="images_topdestination" :index="index" @close="index = null"></gallery>
         </no-ssr>
      <div
        class="image col-sm-3"
        v-for="(image, imageIndex) in images_topdestination"
        :key="imageIndex"
        @click="index = imageIndex"
        :style="{ backgroundImage: 'url(' + image + ')', width: '350px', height: '250px' }"
      ></div>
    </div>

    <!--------------- PARTNERS --------------->
    <div id="div_partners" class="bg-white" style=" width:100%; margin-top:5em;">
      <h2 class="font-weight-hard text-black container mt-5">PARTNERS</h2>
      <div id="div_img_partners" class="row container" style="width:90%; "></div>
      <div style="height:5em;"></div>
    </div>
    <!--------------- SERVICES OFFERED --------------->

    <div id="div_servicesoffered" style=" width:100%; ">
      <h2
        class="font-weight-hard-servicesoffered text-black container"
        style="color:#0b464c !important;"
      >SERVICES OFFERED</h2>
      <div class="row container mt-5" style="width:80%;">
        <div class="col-sm-4">
          <h3 class="custom-text">Reservations</h3>
          <p
            style="font-size: 13px;"
            class
          >Airline Ticketing (Domestic &amp; International). Shipping Lines Ticketing. Hotel Reservation. Car Reservations</p>
        </div>
        <div class="col-lg-4">
          <h3 class="custom-text">Tour Packages</h3>
          <p
            style="font-size: 13px;"
            class
          >City Tours. Adventure Tours. Aquatic Tours. Educational Tours. Group Tours/ Cruise Tours. Land Arrangement</p>
        </div>
        <div class="col-sm-4">
          <h3 class="custom-text">Documentation</h3>
          <p
            style="font-size: 13px;"
            class
          >Online Passport Reservation, Red Ribbon, NSO Online Application. Tourist Visa Application</p>
        </div>
      </div>
      <div class="row container mt-4" style="width:80%;">
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
      <div class="row container mt-4" style="width:90%;">
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
    <!--------------- ABOUT US --------------->
    <div id="div_aboutus" class="bg-white" style=" width:100%; margin-top:5em;">
      <h2 class="font-weight-hard text-black container mt-5">About Us</h2>
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
    <!--------------- GET IN TOUCH --------------->
    <div id="div_getintouch" class style=" width:100%; ">
      <h2 class="font-weight-hard-servicesoffered text-black container">Get In Touch</h2>
      <div class="container">
        <div class="row mt-4" style="width:90%;">
          <div class="col-lg-6">
            <div class="bg-white pl-3 pt-3 pb-3 container" style="heigth:5em;   ">
              <div class="mapouter">
                <div class="gmap_canvas">
                  <iframe
                    width="600"
                    height="500"
                    id="gmap_canvas"
                    src="https://maps.google.com/maps?q=8%20miles%20travel%20corp&t=&z=13&ie=UTF8&iwloc=&output=embed"
                    frameborder="0"
                    scrolling="no"
                    marginheight="0"
                    marginwidth="0"
                  ></iframe>
                </div>
                <style></style>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div
              class="bg-white pl-3 pt-5"
              style="heigth:5em; width:100%; text-align:left; color:#4d4d4d;"
            >
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
      <div style="height:5em;"></div>
    </div>
    <!--------------- PARTNERS --------------->
    <div style=" width:100%; margin-top:5em; background-color:#333333;">
      <div class="row container site-footer pt-5" style="width:90%;">
        <div class="col-sm-6" style="text-align:left;">
          <h3 class="footer-heading mb-4">About 8 miles Travel Corp.</h3>
          <p
            style="font-size: 13px;"
          >8-Miles Travel Corp. is a legit Travel Company that caters all Airline ticketing (Domestic &amp; International flights), Tour Packages, Car Rental Services, Passporting, Tourist Visas etc.</p>
        </div>
        <div class="col-lg-2" style="text-align:left;">
          <h3 class="footer-heading mb-4">Quick Links</h3>
          <ul class="list-unstyled" style="font-size: 13px; color:#737373 !important;">
            <li>
              <a href="#">
                <p>Home</p>
              </a>
            </li>
            <li>
              <a href="#">
                <p>Destination</p>
              </a>
            </li>
            <li>
              <a href="#">
                <p>Services</p>
              </a>
            </li>
            <li>
              <a href="#">
                <p>About</p>
              </a>
            </li>
          </ul>
        </div>
        <div class="col-sm-2" style="text-align:left;">
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
      <div style="height:5em;"></div>
    </div>
    <div class="container">
      <div class="pt-3" style="height:4em; font-size:80%; font-weight:500; width:64%;">
        <a
          href="https://x-mediagraphicsinc.com/"
          target="_blank"
          style="color: black;"
        >X-Media Graphics Inc.</a>
        | MCBI-Trade Corporation | MCBI-Land Corporation |
        <a
          href="https://mcbi-equipments.com/"
          target="_blank"
          style="color:black;"
        >MCBI-Equipments Inc.</a>
      </div>
    </div>

    <!--------------- BODY --------------->
    <div id="Body-content">
      <nuxt />
    </div>

     <!--------------- Inquiries --------------->
<div id="fb-widget" class="fb-widget" style="display: none; bottom: 30px; opacity: 1; ">
            <div class="ctrlq fb-close" @click="fb_close" style="transition: all ease 4s;">X</div>
            <div class="fb-page fb_iframe_widget" data-href="https://www.facebook.com/eightmilestravel/" data-tabs="messages" data-width="360" data-height="400" data-small-header="true" data-hide-cover="true" data-show-facepile="false" fb-xfbml-state="rendered" fb-iframe-plugin-query="app_id=&amp;container_width=0&amp;height=400&amp;hide_cover=true&amp;href=https%3A%2F%2Fwww.facebook.com%2Feightmilestravel%2F&amp;locale=en_US&amp;sdk=joey&amp;show_facepile=false&amp;small_header=true&amp;tabs=messages&amp;width=360"><span style="vertical-align: bottom; width: 360px; height: 400px;"><iframe name="f37bbcb1982089c" width="360px" height="400px" title="fb:page Facebook Social Plugin" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" allow="encrypted-media" src="https://www.facebook.com/v2.12/plugins/page.php?app_id=&amp;channel=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D45%23cb%3Df311e6ef6f7c6d4%26domain%3Deightmilestravel.com%26origin%3Dhttp%253A%252F%252Feightmilestravel.com%252Ff134bcd73988%26relation%3Dparent.parent&amp;container_width=0&amp;height=400&amp;hide_cover=true&amp;href=https%3A%2F%2Fwww.facebook.com%2Feightmilestravel%2F&amp;locale=en_US&amp;sdk=joey&amp;show_facepile=false&amp;small_header=true&amp;tabs=messages&amp;width=360" style="border: none; visibility: visible; width: 360px; height: 400px;" class=""></iframe></span></div>

            <div id="fb-root"></div>
        </div>

    <div id="return-to-topchat"  @click="fbchat"   class=" " style="transition: all ease 2s; background-color:#0084ff; color:white !important;" >
         <i  class="fas fa-comment-dots pt-2" style="font-size:1.7em;"></i>

        <a href="https://m.me/eightmilestravel"  class="ctrlq fb-button" style="right: 70px;"></a>
    </div>




    <!--------------- RETURN TO TOP --------------->
     <!-- botfooter -->
    <div id="return-to-top" @click="topfunction" class="btn btn-warning animated scroll-up-icon" style="transition: all ease 2s;">

      <i id="home-icon" class="material-icons" >local_airport</i>
    </div>
    <!--------------- FOOTER --------------->
    <div id="Footer-content" style="display:none;">
      <div class="row" style="width:100%; height:38em; margin:auto;">
        <div
          class="col-sm-2"
          style="color:yellow; margin-top:12px; font-weight:bolder;"
        >WELCOME USER!</div>
        <div class="col-lg-8 pt-3 text-white" style="font-size: 80%; font-weight: 400;">
          <a
            href="https://x-mediagraphicsinc.com/"
            target="_blank"
            style="color:white;"
          >X-Media Graphics Inc.</a>
          | MCBI-Trade Corporation | MCBI-Land Corporation |
          <a
            href="https://mcbi-equipments.com/"
            target="_blank"
            style="color:white;"
          >MCBI-Equipments Inc.</a>
        </div>
        <div class="col-sm-2 pt-2">
          <span
            class="badge badge-success"
            style="border:0px solid red; margin-left:11.9em; cursor:pointer;"
          >
            Close
            <span class="badge badge-danger" @click="close_footer">X</span>
          </span>
        </div>
      </div>
    </div>

    <!--------------- My Modal --------------->
    <div>
      <b-modal id="modal-register">
        <template v-slot:modal-header="{ }">
          <b size="sm" variant="outline-none">
            <h5>Registration</h5>
          </b>
        </template>
<<<<<<< HEAD

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
=======
        <b-form >
          <div class="row container pt-3">
            <div class="col-md-6">
              <div class="form-group">
                <input type="text" class="form-control" id="agencyName" placeholder="AGENCY NAME"/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input type="text" class="form-control" id="fullName" placeholder="FULLNAME" />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input type="text" class="form-control"  id="emailAddress" placeholder="EMAIL ADDRESS" />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input type="text" class="form-control"  id="contact" placeholder="CONTACT NO."/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input type="text" class="form-control" id="address" placeholder="ADDRESS" />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <input  type="text" class="form-control" id="remarks" placeholder="REMARKS"/>
              </div>
>>>>>>> bcc82d1ec486df3c0abf5f7dddbf088e66ac0872
            </div>
          </div>
        </b-form>

        <template v-slot:modal-footer="{cancel }">
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button type="submit" size="sm" variant="success" @click="save()">Save</b-button>
        </template>
      </b-modal>

      <b-modal id="modal-login">
        <template v-slot:modal-header="{ }">
          <b size="sm" variant="outline-none">
            <h5>LOGIN</h5>
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
                placeholder="USERNAME"
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
                placeholder="PASSWORD"
              />
            </div>
          </div>
        </div>

        <template v-slot:modal-footer="{cancel }">
          <b-button size="sm" variant="danger" @click="cancel()">Cancel</b-button>
          <b-button size="sm" variant="success" @click="ok()">Sign In</b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>


















<!-----------------   SCRIPTS  ------------------>
<script>
require('@/assets/css/custom.css')
import axios from "axios";
import Cookies from "js-cookie";
import $ from "jquery";
import VueGallery from "vue-gallery-slideshow";
export default {
  name: "app",
  components: { gallery: VueGallery },
  data() {
    return {
      images_topdestination: [],
      index: null
    };
  },
  methods: {
    fb_close()
    {
        document.getElementById("fb-widget").classList.remove("viewchat");
    },
    fbchat()
    {
        document.getElementById("fb-widget").classList.toggle("viewchat");
    },
          logintoggle()
          {
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
              Cookies.set("Uname", uname);

<<<<<<< HEAD
              this.$router.push("Dashboard");
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
            document.getElementById("return-to-topchat").classList.remove("botfooter");
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
=======
    btn_sidebar() {
      document.getElementById("sidebar").classList.toggle("sidebar-expand");
      setTimeout(function() {
        document
          .getElementById("sidebar-content")
          .classList.toggle("sidebar-content-show");
      }, 200);
    },
    save(){
      
      console.log($('#agencyName').val())
    },
    ok() {
  
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
>>>>>>> bcc82d1ec486df3c0abf5f7dddbf088e66ac0872
  mounted() {

    axios
      .get(
        
        "http://localhost:5555/api/v1.0/users/"
      )
    
      .then(response => {
        
           console.log(response.data)
        // for (var z = 0; z < response.data.data.length; z++) {
        //   var test = {};
        //   test.id = response.data.data[z].id;
        //   console.log(test.id)
          // var imageLink = require("../assets/img/TopDestination/" +
          //   test.id +
          //   ".jpg");
          // var imgEL = '<img src="' + imageLink + '" class="img-fluid">';
          // this.images_topdestination.push(imageLink);
        // }
      });





    
    
    
    var lcookie = Cookies.get("Uname");
    if (typeof lcookie === "undefined") {
      this.$router.push("/");
    } else {
      this.$router.push("dashboard");
    }
    // -------------------- Top Destination ------------------------
    axios
      .get(
        "https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json"
      )
    
      .then(response => {
        // console.log(response.data)
        for (var z = 0; z < response.data.RECORDS.length; z++) {
          var test = {};
          test.id = response.data.RECORDS[z].id;
          var imageLink = require("../assets/img/TopDestination/" +
            test.id +
            ".jpg");
          var imgEL = '<img src="' + imageLink + '" class="img-fluid">';
          this.images_topdestination.push(imageLink);
        }
      });
    // -------------------- Partners ------------------------
    axios
      .get(
        "https://raw.githubusercontent.com/clavearnel/philippines-region-province-citymun-brgy/master/json/refregion.json"
      )
      .then(response => {
        for (var z = 0; z < response.data.RECORDS.length; z++) {
          var test = {};
          test.id = response.data.RECORDS[z].id;
          if (test.id == "1") {
            var imageLink = require("../assets/img/Partners/" +
              test.id +
              ".png");
            var imgEL =
              '<a class=" col-sm-2  " href="https://mcbi-equipments.com/" target="_blank"> <img src="' +
              imageLink +
              '" class="img-fluid   imagepartners" title="MCBI EQUIPMENT"  > </a>';
            $("#div_img_partners").append(imgEL);
          } else if (test.id == "2") {
            var imageLink = require("../assets/img/Partners/" +
              test.id +
              ".png");
            var imgEL =
              '<a class=" col-sm-2  " > <img src="' +
              imageLink +
              '" class="img-fluid   imagepartners" title="MCBI TRADE CORPORATION"  > </a>';
            $("#div_img_partners").append(imgEL);
          } else if (test.id == "3") {
            var imageLink = require("../assets/img/Partners/" +
              test.id +
              ".png");
            var imgEL =
              '<a class=" col-sm-2  " > <img src="' +
              imageLink +
              '" class="img-fluid   imagepartners" title="MCBI LAND CORPORATION"  > </a>';
            $("#div_img_partners").append(imgEL);
          } else if (test.id == "4") {
            var imageLink = require("../assets/img/Partners/" +
              test.id +
              ".png");
            var imgEL =
              '<a class=" col-sm-2  " href="https://x-mediagraphicsinc.com/" target="_blank"> <img src="' +
              imageLink +
              '" class="img-fluid   imagepartners" title="X-MEDIA GRAPHICS INC."  > </a>';
            $("#div_img_partners").append(imgEL);
          } else {
            var imageLink = require("../assets/img/Partners/" +
              test.id +
              ".png");
            var imgEL =
              '<img src="' +
              imageLink +
              '" class="img-fluid col-sm-2  imagepartners" >';
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

          document.getElementById("return-to-topchat").style.marginRight ="4em";
          navBar.classList.add("sticky-top");
          document.getElementById("return-to-top").style.display = "block";
          btnsidebar.classList.add("btn-sidebarscroll");
          btntogglers.classList.add("navbar-togglerscroll");
          sidebars.classList.add("sidebarscroll");
        } else {
          document.getElementById("return-to-topchat").style.marginRight ="0em";
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



