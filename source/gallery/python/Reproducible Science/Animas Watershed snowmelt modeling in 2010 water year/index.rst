.. _a2b87a2f25d046958ac604e522f449c0:

.. title:: Animas watershed snowmelt modeling in the 2010 water year (use case 2)

.. raw:: html

    <div class=example-title>
        <h1> Animas watershed snowmelt modeling in the 2010 water year (use case 2) </h1>
    </div>






.. container:: container-lg launch-container pb-1

    
         
            :link-badge:`https://hydroshare.org/resource/a2b87a2f25d046958ac604e522f449c0,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    



.. container:: container-lg launch-container pb-1 author-div
    
    .. raw:: html

        <br />&nbsp;
        <hr>
        <br />&nbsp;
        <h2> Authors </h2>

            

            <span class="NameHighlights">
                <a href="javascript:;">Tian Gan</a>
                
                <div>

                    Utah State University 

                    <hr>

                    

                        <a class="sphinx-bs badge badge-primary text-white reference external" href=mailto:jamy127@foxmail.com>
                            <span>Email</span>
                        </a>

                    


                    

                </div>
            </span>

        


.. raw:: html

    <br />&nbsp;
    <br />&nbsp;

    <div class=example-description>
    
    <h2> Description </h2>

    
    
    <p>This resource contains the use case results of web-based simulation for snowmelt modeling research. The model input files were created by executing the Python script (ueb_setup.py) in CUAHSI JupyterHub web app, which made web requests to HydroDS modeling web services (https://github.com/CI-WATER/Hydro-DS) for inputs preparation. The model output files were created by using the model input files and the UEB web app (https://appsdev.hydroshare.org/apps/ueb-app/). A JupyterHub Notebook file (Data_analysis_code.ipynb) includes the data analysis code to compare the model output created by this use case and another use case (https://doi.org/10.4211/hs.1be4d7902c87481d85b93daad99cf471) with different model grid resolutions (600 m vs 1200 m).</p>
    
    
    
    </div>


.. raw:: html

    <h2> Code </h2>


.. panels::
    :container: container pb-1 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left

    ---
    

       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 1
        :titlesonly:
        :glob:
        
        
        ./notebooks/**
        
     
     
