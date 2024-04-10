# Workshop Program

The workshop will take place during the 2024 Vision Sciences Society meeting on
Monday, May 20th, from 2:00-5:00pm in the Banyan/Citrus room. (The workshop is
neither sponsored nor endorsed by VSS.) The program will consist of three
presentations, each lasting slightly under an hour, with short breaks between.

**The goal of this program is to introduce participants to contemporary data
science/neuroscience software tools and to give them enough initial experience
to be able to apply them in their own research.** We cannot teach everything
about any tool in a three hour workshop, but through hands-on tutorials and
follow-along coding, we intend to help participants past the hardest part of the
learning process: getting started. In addition to learning about neuroscience
software, participants will receive 1 month of access to a virtual compute
environment preconfigured using the [Neurodesk](https://neurodesk.org/) platform
with the software discussed in the workshop. Use of this computing environment
requires only a modern web browser and a GitHub username. Tutorials and lectures
will be made available to the public.

**Tutorials for the course will be made public in the [accompanying GitHub
repository]({{ site.githuburl }}).** See the README file there for information
on running them either using the workshop's compute environment or on your own.
Lecture recordings will also be posted here.


## Curriculum

### How to stop worrying about software

*Mark M. Schira*

<!-- Insert abstract / edit title here! -->
This talk will introduce the web based neurodesk instance and how to access it. It will then cover the basics of Neurodesk and why it is useful for computational neuroscience. It will then cover how to seamlessly move a project between a local workstation, a cloud instance of neurodesk and a high performance cluster based on the example of the Human Brain Atlas project. Finally, the session will discuss experiences on using a cloud based Neurodesk instance for teaching 45 undergraduate computer novices the basics of MRI analysis.

1. **The cloud based Neurodesk instance**
* [`Play`](https://www.neurodesk.org/docs/getting-started/neurodesktop/play/)

2. **What is Neurodesk and why should I care**
* [`Neurodesk`](https://www.neurodesk.org/)
3. **Using a HPC system**
  * The [`HBA project`](hba.neura.edu.org)
  * Making [`data`](https://osf.io/ckh5t/) available on OSF.io
4. **Herding cats**
  * teaching undergraduates using a cloud neurodesk




### A reproducible pipeline for visual neuroimaging

*Noah C. Benson*

This talk will discuss and show example usage for standard software tools that
together build a functional MRI pipeline for processing retinotopic mapping
experiments in a reproducible way. The session will end by demonstrating tools
for drawing visual area boundaries.

1. **Introduction and Dataset Description**
2. **Preprocessing the Data**
  * The Brain Imaging Data Structure ([`BIDS`](https://bids.neuroimaging.io/))
  * [`fMRIprep`](https://fmriprep.org/en/stable/)
3. **Modeling the Visual Responses**
  * Population Receptive Field (pRF) models and General Linear Models (GLMs)
  * [`PRFModel`](https://github.com/vistalab/PRFModel)
4. **Annotating the Visual Cortex**
  * Retinotopic maps and boundaries
  * [`cortex-annotate`](https://github.com/noahbenson/cortex-annotate)


### Machine learning and automation in the visual cortex

*Fernanda L. Ribeiro*

In this final session, we will introduce deepRetinotopy and demonstrate its command line interface to predict retinotopic maps using FreeSurfer derivatives. Then, we perform a visual field sign analysis to guide delineating visual area boundaries.

1. **Predicting retinotopic maps with deepRetinotopy**
  * Polar angle and eccentricity maps
  * [`deepRetinotopy`](https://github.com/felenitaribeiro/deepRetinotopy_TheToolbox)
3. **Visual field sign analysis**
  * Binary representation of visual areas where adjacent visual areas have distinct field signs
  * [`deepRetinotopy`](https://github.com/felenitaribeiro/deepRetinotopy_TheToolbox)
    
<!-- Insert abstract / edit title here! -->
