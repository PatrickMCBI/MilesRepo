<template>
    <div>
       
  <div class="container mt-5 pt-5 pb-5" style="box-shadow: 0px 0px 3px 0px rgb(24, 23, 23); background-color:#f2f3f7 !important;">
              <div class="row container ">
                            <div class="col-md-12" >
                              <div class="form-group text-center" >
                               <h2 style="color:#636363; font-weight:700; font-size: 30px;  ">Register</h2>
                               </div>
                            </div>
                             <div class="col-md-4" >
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Agency Name</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Fullname</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Email Address</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Contact #</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Address</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Remarks</label>
                                </div>
                            </div>
                             <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Remarks</label>
                                </div>
                            </div>
                              <div class="col-md-4">
                                <div class="form-group searchformfld" style="background-color:#f2f3f7 !important;">
                                <input type="text" class="form-control" placeholder=" "  />
                                <label style="color:#636363;">Remarks</label>
                                </div>
                            </div>
                            <!-- <div class="input-group col-md-5 searchformfld">
                            <div class="input-group-prepend">
                                <select class="form-control input-group-text repGender">
                                    <option value="1">Mr</option>
                                    <option value="2">Ms</option>
                                </select>
                            </div>
                            <input type="text" class="form-control RepFirstName" placeholder=" " id="RepFirstName" />
                            <label for="RepFirstName" style="margin-left:65px;">FirstName</label>
                        </div> -->
                             <div class="col-md-12">
                              <div class="form-group">
                               <button class="btn btn-success " style="float:right; font-weight:700">Register Now</button>
                              </div>
                            </div>
                            </div>

  </div>
            
    </div>
</template>



<style>
.img-leftlogo {
    width: 10em;
    margin-left: 0em;
}
body{
  background-color:#63738a !important;
}
/* ---------------------- */
.searchformfld label {
        position: absolute;
        padding-left: 10px;
        top: 15px;
        opacity: 1.5;
    }
    .searchformfld input:focus + label, .searchformfld input:not(:placeholder-shown) + label{
        opacity: 1;
        transform: scale(.9) translateY(-100%) translateX(-10px);
        color: #000;
    }
    .searchformfld input:focus {
        border: 1px solid #000;
        outline-color: #000;
        background-color: #fff !important;
    }
.searchformfld {
    padding: 12.4px;
    margin: 15px 0px;
    position: relative;
    background-color: #FFFFFF;
}
    .searchformfld input {
        width: 100%;
        padding-left: 10px;
        color: #000 !important;
    }
    .searchformfld label, .searchformfld input {
        transition: all 0.2s;
        transition-timing-function: ease;
        transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1);
        /*opacity: 0.5;*/
    }
.a {
    text-indent: 66px;
}
.nav.fa {
    transition: .3s transform ease-in-out;
}
.nav[aria-expanded=true] {
    transform: rotate(-90deg);
}
    /*.searchformfld {
    position: relative;
    margin: 5px 0px;
}*/
@media (min-width: 1340px)
{
      .container 
      {
          max-width: 1140px;
      }
}
</style>