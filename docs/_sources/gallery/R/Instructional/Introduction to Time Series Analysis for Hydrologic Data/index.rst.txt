.. _ee2a4c2151f24115a12e34d4d22d96fe:

.. title:: Introduction to Time Series Analysis for Hydrologic Data

.. raw:: html

    <div class=example-title>
        <h1> Introduction to Time Series Analysis for Hydrologic Data </h1>
    </div>






.. container:: container-lg launch-container pb-1
    
         
            :link-badge:`https://hydroshare.org/resource/ee2a4c2151f24115a12e34d4d22d96fe,"Open In HydroShare",cls=badge-primary text-white launch-badge`
        
    

.. raw:: html

    <br />&nbsp;
    <hr>
    <br />&nbsp;

    <h2> Authors </h2>

    

    <span class="NameHighlights">
        <a href="javascript:;">Salk, Kateri</a>
        
            , 
        
        <div>

            Duke University 

            <hr>

            
                
                <a class="sphinx-bs badge badge-primary text-white reference external" href=mailto:kateri.salk@duke.edu>
                    <span>Email</span>
                </a>
            
            

            
            
                
                <a class="sphinx-bs badge badge-primary text-white reference external" href=https://hydroshare.org/user/4912/>
                    <span>Webpage</span>
                </a>

            

        </div>
    </span>

    

    <span class="NameHighlights">
        <a href="javascript:;">Garcia, Gabriela</a>
        
        <div>

            Duke University 

            <hr>

            
                
                <a class="sphinx-bs badge badge-primary text-white reference external" href=mailto:gabriela.garcia@duke.edu>
                    <span>Email</span>
                </a>
            
            

            
            
                
                <a class="sphinx-bs badge badge-primary text-white reference external" href=https://hydroshare.org/user/7399/>
                    <span>Webpage</span>
                </a>

            

        </div>
    </span>





.. raw:: html

    <br />&nbsp;
    <br />&nbsp;

    <div class=example-description>
    
    <h2> Description </h2>

    
    
    <p>This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the first part of a two-part exercise focusing on time series analysis. <br><br> Introduction<br><br>Time series are a special class of dataset, where a response variable is tracked over time. The frequency of measurement and the timespan of the dataset can vary widely. At its most simple, a time series model includes an explanatory time component and a response variable. Mixed models can include additional explanatory variables (check out the `nlme` and `lme4` R packages). We will be covering a few simple applications of time series analysis in these lessons.<br><br>Opportunities<br><br>Analysis of time series presents several opportunities. In aquatic sciences, some of the most common questions we can answer with time series modeling are:<br><br>* Has there been an increasing or decreasing trend in the response variable over time?<br>* Can we forecast conditions in the future?<br><br><br> Challenges<br><br>Time series datasets come with several caveats, which need to be addressed in order to effectively model the system. A few common challenges that arise (and can occur together within a single dataset) are: <br><br>* Autocorrelation: Data points are not independent from one another (i.e., the measurement at a given time point is dependent on previous time point(s)).<br><br>* Data gaps: Data are not collected at regular intervals, necessitating *interpolation* between measurements. There are often gaps between monitoring periods. For many time series analyses, we need equally spaced points. <br><br>* Seasonality: Cyclic patterns in variables occur at regular intervals, impeding clear interpretation of a monotonic (unidirectional) trend. Ex. We can assume that summer temperatures are higher.<br><br>* Heteroscedasticity: The variance of the time series is not constant over time.<br><br>* Covariance: the covariance of the time series is not constant over time. Many of these models assume that the variance and covariance are similar over the time-->heteroschedasticity. <br><br> Learning Objectives<br><br>After successfully completing this notebook, you will be able to:<br><br>1. Choose appropriate time series analyses for trend detection and forecasting<br><br>2. Discuss the influence of seasonality on time series analysis<br><br>3. Interpret and communicate results of time series analyses</p>
    
    
    
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
        
     
     
