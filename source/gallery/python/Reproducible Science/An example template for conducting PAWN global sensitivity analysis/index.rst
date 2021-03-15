.. _bae3f93a5dc54dd886729265eecc784f:

.. title:: An example template for conducting PAWN global sensitivity analysis on parameters of the PRMS model using the PRMS-Python framework

.. raw:: html

    <div class=example-title>
        <h1> An example template for conducting PAWN global sensitivity analysis on parameters of the PRMS model using the PRMS-Python framework </h1>
    </div>





.. container:: launch-container pb-1
    
         
            :link-badge:`https://hydroshare.org/resource/bae3f93a5dc54dd886729265eecc784f,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    

.. raw:: html

    <br />&nbsp;
    <hr>
    <br />&nbsp;

.. raw:: html

    <div class=example-description>
        <h2> Description </h2>
        <p>Global sensitivity analysis GSA is a useful tool for diagnosing and quantifying uncertainty within hydrologic models.  Facilitating advanced model analyses such as GSA of parameters has the potential to help advance our fundamental understanding of hydrologic process representations. This document acts as a working template to apply a GSA method for parameters of the well-known Preceipitation-Runoff Modeling System (PRMS) hydrologic model maintained by the United States Geological Survey.  Specifically, it documents a workflow for a moment-independent, GSA method based on empirical cumulative distribution functions named PAWN. The template is a Jupyter notebook that uses an open-source Python package called PRMS-Python; installation instructions for PRMS-Python and links to both PAWN and the Python software are included. PRMS-Python has  a built in routine for Monte Carlo parameter resampling that this template demonstrates and uses to implement PAWN. The template is written so that it could be modified for an arbitrary set of PRMS parameters and is heavily commented for clarity.  As such, this template along with the open-source Python package aim to  encourage and facilitate the greater hydrologic modeling community to conduct advanced model analyses such as GSA. Similarly, the PRMS-Python framework has tools for self-generation of metadata files that track data provenance of large model ensembles- a useful tool for sharing model results on platforms such as HydroShare. </p>
    </div>







.. panels::
    :container: container pb-2 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left


    ---
      **Authors**
      ^^^^^
    
        :link-badge:`https://hydroshare.org/user/3192/,"John Volk",cls=badge-primary text-white`
        - University of Nevada Reno 
        (`contact <johnvolk08@gmail.com>`_)
        


    ---
    

       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 1
        :titlesonly:
        :glob:
        
        
        ./notebooks/**
        
     
     
