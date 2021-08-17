.. _bae3f93a5dc54dd886729265eecc784f:

.. title:: An example template for conducting PAWN global sensitivity analysis on parameters of the PRMS model using the PRMS-Python framework

.. raw:: html

    <div class=example-title>
        <h1> An example template for conducting PAWN global sensitivity analysis on parameters of the PRMS model using the PRMS-Python framework </h1>
    </div>






.. container:: container-lg launch-container pb-1

    
         
            :link-badge:`https://hydroshare.org/resource/bae3f93a5dc54dd886729265eecc784f,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    



.. container:: container-lg launch-container pb-1 author-div
    
    .. raw:: html

        <br />&nbsp;
        <hr>
        <br />&nbsp;
        <h2> Authors </h2>

            

            <span class="NameHighlights">
                <a href="javascript:;">John Volk</a>
                
                <div>

                    University of Nevada Reno 

                    <hr>

                    

                        <a class="sphinx-bs badge badge-primary text-white reference external" href=mailto:johnvolk08@gmail.com>
                            <span>Email</span>
                        </a>

                    


                    

                        <a class="sphinx-bs badge badge-primary text-white reference external" href=https://hydroshare.org/user/3192/>
                            <span>Profile</span>
                        </a>

                    
                    <!-- TODO: Include personal webpages from conf.yaml -->

                </div>
            </span>

        


.. raw:: html

    <br />&nbsp;
    <br />&nbsp;


.. tabs::
    
    .. tab:: Description

        
    
        .. raw:: html
        
            Global sensitivity analysis GSA is a useful tool for diagnosing and quantifying uncertainty within hydrologic models.  Facilitating advanced model analyses such as GSA of parameters has the potential to help advance our fundamental understanding of hydrologic process representations. This document acts as a working template to apply a GSA method for parameters of the well-known Preceipitation-Runoff Modeling System (PRMS) hydrologic model maintained by the United States Geological Survey.  Specifically, it documents a workflow for a moment-independent, GSA method based on empirical cumulative distribution functions named PAWN. The template is a Jupyter notebook that uses an open-source Python package called PRMS-Python; installation instructions for PRMS-Python and links to both PAWN and the Python software are included. PRMS-Python has  a built in routine for Monte Carlo parameter resampling that this template demonstrates and uses to implement PAWN. The template is written so that it could be modified for an arbitrary set of PRMS parameters and is heavily commented for clarity.  As such, this template along with the open-source Python package aim to  encourage and facilitate the greater hydrologic modeling community to conduct advanced model analyses such as GSA. Similarly, the PRMS-Python framework has tools for self-generation of metadata files that track data provenance of large model ensembles- a useful tool for sharing model results on platforms such as HydroShare. 

    
        

    .. tab:: Code 


        
        .. toctree::
            :maxdepth: 1
            :titlesonly:
            :glob:
     
            
            ./notebooks/**
            

        

        

    