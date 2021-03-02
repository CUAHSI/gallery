.. _cad5dd0c4106489e87db2e8366dd66b1:

.. raw:: html

    <div class=example-title>
        <h1> HydroDS UEB model input setup Python scripts </h1>
    </div>





.. container:: launch-container pb-1
    
         
            :link-badge:`https://hydroshare.org/resource/cad5dd0c4106489e87db2e8366dd66b1,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    

.. raw:: html

    <br />&nbsp;
    <hr>
    <br />&nbsp;

.. raw:: html

    <div class=example-description>
        <h2> Description </h2>
        <p>The HydroDS tasks required to be executed to get complete UEB model inputs for an example watershed are given in the Python file HydroDS_UEB_Setup. This file calls functions from the other file, "hydrods_python_client" that has declarations for data service functions available from HydroDS. <br><br>To run the workflow for a different watershed in the Western US, modify the coordinates of the watershed boundary, outlet location, the start and end time of model period, and the spatial reference (projection) information in the form of EPSG Code (http://spatialreference.org/ref/epsg/). The commands in the workflow script can also be called interactively from any Python command line, or from a user application that uses incorporates the Python Client Library. <br><br>For watersheds outside of the Western US, but in the CONUS, you need to upload your own DEM. The services are currently limited to the US. <br>You need to have a HydroDS account to use these services.<br><br>These scripts are for the following paper<br>Gichamo, T. Z., N. S. Sazib, D. G. Tarboton and P. Dash, (2020), "HydroDS: Data Services in Support of Physically Based, Distributed Hydrological Models," Environmental Modelling & Software, https://doi.org/10.1016/j.envsoft.2020.104623.</p>
    </div>







.. panels::
    :container: container pb-2 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left


    ---
      **Authors**
      ^^^^^
    
        :link-badge:`https://hydroshare.org/user/15/,"Tseganeh Gichamo",cls=badge-primary text-white`
        -  
        (`contact <zacctsega@gmail.com>`_)
        
        :link-badge:`https://hydroshare.org/user/2/,"Tarboton, David",cls=badge-primary text-white`
        - Utah State University 
        (`contact <dtarb@usu.edu>`_)
        
        :link-badge:`https://hydroshare.org/user/41/,"Dash, Pabitra",cls=badge-primary text-white`
        - USU 
        (`contact <pabitra.dash@usu.edu>`_)
        


    ---
    

       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 1
        :titlesonly:
        :glob:
        
        
        ./notebooks/**
        
     
     
