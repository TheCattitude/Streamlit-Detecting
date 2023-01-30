
# Streamlit - Detecting

Frontend for the final project of Le Wagon Data Science Bootcamp December 2022

This GitHub repository complements the repository [Detecting Far Right Talking Points In Political Speeches](https://github.com/konratp/Detecting-Far-Right-Talking-Points). It contains the frontend (API, Streamlit website, Docker) for the machine learning backend of the project. 

Our [website](https://thecattitude-streamlit-det-our-apistreamlitweb-interface-ksrpd8.streamlit.app/) allows users to input the text of a speech and find out whether our machine learning model classifies the speech as far right. 

## Description of the Project

This repository includes code for the final project for [Le Wagon's Data Science Bootcamp](https://www.lewagon.com/data-science-course?utm_term=le wagon courses&utm_campaign=WW+|+Brand+|+EN+|+S&utm_source=adwords&utm_medium=ppc&hsa_acc=9887519486&hsa_cam=17795863130&hsa_grp=138703896883&hsa_ad=634543295246&hsa_src=g&hsa_tgt=kwd-811252777396&hsa_kw=le wagon courses&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiAveebBhD_ARIsAFaAvrHtFXBTG6fge-2tThnAgAJx13gnibCR00eBIoS6UaoLbzPT3ZjTtFQaAogiEALw_wcB) (Batch 1014) in Berlin. Using over 144,000 speeches given in the European Parliament between 1996 and 2011, we attempt to understand when politicians from liberal, conservative, environmentalist and leftist parties evoke far-right talking points. To achieve this, we trained a deep learning classifier to predict if a given speech was given by a far-right politician or not. We then performed topic modeling on the subset of speeches our model falsely classified as far-right, i.e. our model detected far-right rhetoric, but the speech itself was not given by a far-right Member of the European Parliament (MEP). We presented the our findings at Le Wagon's Demo Day 2022, feel free to watch our presentation using [this link](https://drive.google.com/file/d/1NcrEVAfzOHh2Q9QShYnqyt-CDaIdGCqu/view?usp=sharing). The code in this repository was co-authored by [Odelia Ahdout](https://www.linkedin.com/in/odelia-ahdout-phd-824237218/), [Elena Malysheva](https://www.linkedin.com/in/malysheva42/), [Konrat Pekkip](https://www.linkedin.com/in/konratpekkip/) and [Viktoria Bentley](https://www.linkedin.com/in/viktoria-bentley/).

## Data

The data for our project stems from the [European Parliament Proceedings Parallel Corpus (1996-2011)](https://www.statmt.org/europarl/) and can be downloaded using [this link](https://www.statmt.org/europarl/#:~:text=Download-,source release,-(text files)%2C 1.5). 

## References

Salvati, Eugenio, 2022, "Replication Data for: Dataset on Members of the European Parliament (1979-2019)", https://doi.org/10.7910/DVN/V2FJEF, Harvard Dataverse, V2

