.. _5148675c6a5841e686a3b6aec67a38ee:

.. raw:: html

    <div class=example-title>
        <h1> Data and models for exploring real-time control of stormwater systems for mitigating flood risk due to sea level rise </h1>
    </div>





.. container:: launch-container pb-1
    
         
            :link-badge:`https://hydroshare.org/resource/5148675c6a5841e686a3b6aec67a38ee,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    

.. raw:: html

    <br />&nbsp;
    <hr>
    <br />&nbsp;

.. raw:: html

    <div class=example-description>
        <h2> Description </h2>
        <p>This resource contains data and models that were used to produce results for a paper published in the Journal of Hydrology. The models are for a neighborhood in Norfolk, Virginia USA that suffers from frequent coastal flooding. The paper describes the use of active stormwater controls to mitigate this problem which will worsen with sea level rise. The particular type of control approach explored was model predictive control (MPC) and the Stormwater Management Model (SWMM) was used to simulate the stormwater system. The swmm_mpc Python package (https://github.com/UVAdMIST/swmm_mpc) was used to simulate MPC in the SWMM model. MPC was simulated for a number of sea level rise scenarios and the amount of flooding was compared to the system with no controls. The Python script that ran swmm_mpc for the sea level rise scenarios is "models/runs/hgv11.py." The results were compiled and plotted with scripts in the "models/results/" directory. <br><br>The citation to the Journal of Hydrology paper is<br>Jeffrey M. Sadler, Jonathan L. Goodall, Madhur Behl, Benjamin D. Bowes, Mohamed M. Morsy, Exploring real-time control of stormwater systems for mitigating flood risk due to sea level rise, Journal of Hydrology, Volume 583, 2020, 124571, ISSN 0022-1694, https://doi.org/10.1016/j.jhydrol.2020.124571.</p>
    </div>







.. panels::
    :container: container pb-2 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left


    ---
      **Authors**
      ^^^^^
    
        :link-badge:`https://hydroshare.org/user/320/,"Sadler, Jeff ",cls=badge-primary text-white`
        - University of Virginia 
        (`contact <jms3fb@virginia.edu>`_)
        


    ---
    

       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 1
        :titlesonly:
        :glob:
        
        
        ./notebooks/**
        
     
     
