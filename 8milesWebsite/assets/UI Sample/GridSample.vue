<template>
    <div>
        
            <div id="gridview">
                <div>left</div> <div>center</div> <div>right</div>
                <div id="leftside">leftside</div> <div id="main">MAIN</div> <div id="rightside">rightside</div>
            </div>
            <div id="footer">
                <div>footer</div>
            </div> 
    </div>
</template>

<style>
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