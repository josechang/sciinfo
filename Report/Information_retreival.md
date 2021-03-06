﻿All information retreival  data is recorded.

Elements of Text similarity:

Similarity threshold:
The similarity threshold is a lower limit for the similarity of two data records that belong to the same cluster. 
>>For example, if you set the similarity threshold to 0.25, data records with field values that are 25% similar are likely to be assigned to the same cluster.
If you specify a similarity threshold of 1.0, you are insisting that, for customers to appear in the same group, their characteristics must be identical.
You might have a large number of customer characteristic variables, or the variables might take a wide range of values.
The right setting is somewhere in between, but where?... You have to preserve a balance between the number of clusters that is acceptable and the degree of similarity.
There is another important factor that the Distribution-based Clustering algorithm has to consider.
A situation might occur where you try to give the Distribution-based Clustering algorithm a similarity threshold,and you do not limit the number of clusters that it can produce.
In this case, it will keep trying to find the minimum number of clusters that satisfy the similarity threshold, because this also maximizes the Condorcet value.
In a different situation, you might have limited the number of clusters with the result that, after all the possible clusters are created, a record does not have a similarity above the threshold with any of them.
In this case, the record will be assigned to the cluster with the best similarity, even if the similarity threshold is not reached.

Distribution-based Clustering:
Distribution-based Clustering provides fast and natural clustering of very large databases.
It automatically determines the number of clusters to be generated.
Typically, demographic data consists of large amounts of categorical variables. 
Therefore the mining function works best with data sets that consist of this type of variables.
You can also use numerical variables. 
The Distribution-based Clustering algorithm treats numerical variables almost like categorical variables by categorizing their values into buckets.
Distribution-based Clustering is an iterative process over the input data. 
Each input record is read in succession. 
The similarity of each record with each of the currently existing clusters is calculated. 
Initially, no clusters exist. 
If the biggest calculated similarity is above a given threshold, the record is added to the relevant cluster. 
This cluster's characteristics change accordingly.
If the calculated similarity is not above the threshold, or if there is no cluster, a new cluster is created, containing the record alone.
You can specify the maximum number of clusters, as well as the similarity threshold.
Distribution-based Clustering uses the statistical Condorcet criteria to manage the calculation of the similarity between records and other records, between records and clusters, and between clusters and other clusters. 
The Condorcet criteria evaluates how homogeneous each discovered cluster is (in that the records it contains are similar) and how heterogeneous the discovered clusters are among each other. 
The iterative process of discovering clusters stops after one or more passes over the input data if there is no time remaining to do another pass or if the improvement of the clusters according to the Condorcet criteria would not justify a new pass.

Similarity scale:
The similarity between two data records sums the similarities between each pair of values of these records.
For a categorical field, the similarity is 0 if both values are different, and 1 if they are equal.
For a numerical field, the similarity depends on the difference between the two values compared with the similarity scale of the field. 
If the two values are equal, the similarity is 1. If the two values are distant from the similarity scale, the similarity is 0.5. 
Other values of the similarity are calculated using a Gaussian curve passing through these two reference points.
You can choose to specify a similarity scale or not. 
You specify the similarity scale as an absolute number. The specification is considered only for active numerical fields. If you do not specify a similarity scale, the default value (half of the standard deviation) is used.

Similarity matrices:
For each categorical field, you can define a similarity matrix that contains user-defined similarities between two field values.
A similarity matrix is represented as a reference to a database table containing three columns. 
Two columns contain the field values to be compared, and the third column contains the similarity (between 0 and 1) for these field values.
You can specify the similarity for each pair of possible values. 
A pair of possible values can be used only once. 
The similarity of the inverse pair is the same.

Field weighting:
Field weighting gives more or less weight to certain input fields during a Clustering training run.
>>For example, to identify different types of shoppers, you might not want to give too much weight to the strong correlation between the number of purchases and the total purchase amount. 
Therefore you assign a smaller weight to the fields Number of purchases and Total purchase amount.
The following table shows the decreased field weights for the fields Number of purchases and the Total purchase amount.

Value weighting:
Value weighting deals with the fact that particular values in a field might be more common than other values in that field. 
The coincidence of rare values in a field adds more to the overall similarity than the coincidence of frequent values.
>>For example, most people do not have a Gold credit card. 
It is not very significant if two people do not have one, however, if they do, it is significant. 
Therefore, the coincidence of people not having a Gold credit card adds less to their overall similarity than the coincidence of people having one.
You can use one of the following types of value weighting:

Probability weighting:
Probability weighting assigns a weight to each value according to its probability in the input data. Rare values carry a large weight, while common values carry a small weight. This weight is used for both matching and non-matching records.
Probability weighting uses a factor of 1/root of p, where p is the probability of a value.

Logarithmic weighting:
Logarithmic weighting assigns a weight to each value according to the logarithm of its probability in the input data.
 Rare values carry a large weight, while common values carry a small weight. 
This weight is used for both matching and non-matching records.
Logarithmic weighting assigns a value of root of (-log(p)) to both the agreement information content value and the disagreement information content value. 
The number p is the probability of a value.
Each type of value weighting looks at a problem from a different angle.
Depending on the value distribution, using one type or the other might lead to very different results. 
For example, if a supermarket is located in a retirement community, a Senior discount field has a high probability of having the value Yes. 
You might use probabilistic value weighting to assign a weight to the values in the Senior discount field that is equal to its probability in the input data.
Value weighting has the additional effect of emphasizing fields with many values because their values are less frequent than those of fields with fewer possible values. 
By default, the mining function does not compensate for this additional effect.
You can select whether you want to compensate for the value weighting applied to each field. 
If you compensate for value weighting, the overall importance of the weighted field is equal to that of an unweighted field. 
This is so regardless of the number of possible values. 
Compensated weighting affects only the relative importance of coincidences within the set of possible values.

Maximum number of distribution-based clusters:
You can control the number of clusters to be created during a Clustering training run by specifying a value for the maximum number of clusters.
 Limiting the number of clusters prevents the production of many small clusters, and thus saves run time.
By default, the Distribution-based Clustering algorithm does not create an unlimited number of clusters but sets itself a limit.
If the mining function cannot continue to create clusters because the cluster limit is reached, this may prevent further improvement in the accuracy of the model.
Increasing the number of clusters improves the likelihood of finding market niches.

UNIFIED MODELING LANGUAGE:

Introduction to OMG UML by Dr. Jon Siegel, OMG

Large enterprise applications-the ones that execute core business applications, and keep a company going-must be more than just a bunch of code modules. 
They must be structured in a way that enables scalability, security, and robust execution under stressful conditions, and their structure - frequently referred to as their architecture - must be defined clearly enough that maintenance programmers can (quickly!). 
find and fix a bug that shows up long after the original authors have moved on to other projects. 
That is, these programs must be designed to work perfectly in many areas, and business functionality is not the only one (although it certainly is the essential core).
Of course a well-designed architecture benefits any program, and not just the largest ones as we've singled out here. 
We mentioned large applications first because structure is a way of dealing with complexity.
so the benefits of structure (and of modeling and design, as we'll demonstrate) compound as application size grows large. 
Another benefit of structure is that it enables code reuse: Design time is the easiest time to structure an application as a collection of self-contained modules or components.
Eventually, enterprises build up a library of models of components, each one representing an implementation stored in a library of code modules. 
When another application needs the same functionality, the designer can quickly import its module from the library. 
At coding time, the developer can just as quickly import the code module into the application. 

Modeling is the designing of software applications before coding. 
Modeling is an Essential Part of large software projects, and helpful to medium and even small projects as well. 
A model plays the analogous role in software development that blueprints and other plans (site maps, elevations, physical models) play in the building of a skyscraper.
Using a model, those responsible for a software development project's success can assure themselves that business functionality is complete and correct, end-user needs are met, and program design supports requirements for scalability, robustness, security, extendibility, and other characteristics, before implementation in code renders changes difficult and expensive to make.
Surveys show that large software projects have a huge probability of failure - in fact, it's more likely that a large software application will fail to meet all of its requirements on time and on budget than that it will succeed. 
If you're running one of these projects, you need to do all you can to increase the odds for success, and modeling is the only way to visualize your design and check it against requirements before your crew starts to code.

YOU CAN DO OTHER USEFUL THINGS WITH UML TOO:
some tools analyze existing source code (or, some claim, object code!) and reverse-engineer it into a set of UML diagrams. 
>>Another example: Some tools on the market execute UML models, typically in one of two ways: Some tools execute your model interpretively in a way that lets you confirm that it really does what you want, but without the scalability and speed that you'll need in your deployed application. 
Other tools (typically designed to work only within a restricted application domain such as telecommunications or finance) generate program language code from UML, producing most of a bug-free, deployable application that runs quickly if the code generator incorporates best-practice scalable patterns for, e.g., transactional database operations or other common program tasks. 
(OMG members are working on a specification for Executable UML now.) 
Our final entry in this category: A number of tools on the market generate Test and Verification Suites from UML models. 

MODELS VS. METHODOLOGIES:
The process of gathering and analyzing an application's requirements, and incorporating them into a program design, is a complex one and the industry currently supports many methodologies that define formal procedures specifying how to go about it. 
One characteristic of UML - in fact, the one that enables the widespread industry support that the language enjoys - is that it is methodology-independent. 
Regardless of the methodology that you use to perform your analysis and design, you can use UML to express the results. 
And, using XMI® (XML™ Metadata Interchange, another OMG standard), you can transfer your UML model from one tool into a repository, or into another tool for refinement or the next step in your chosen development process. 
These are the benefits of standardization!.

WHAT CAN YOU MODEL WITH UML?
UML 2.0 defines thirteen types of diagrams, divided into three categories: Six diagram types represent static application structure; three represent general types of behavior; and four represent different aspects of interactions:
Structure Diagrams:  include the Class Diagram, Object Diagram, Component Diagram, Composite Structure Diagram, Package Diagram, and Deployment Diagram.
Behavior Diagrams:  include the Use Case Diagram (used by some methodologies during requirements gathering); Activity Diagram, and State Machine Diagram. 
Interaction Diagrams:  all derived from the more general Behavior Diagram, include the Sequence Diagram, Communication Diagram, Timing Diagram, and Interaction Overview Diagram.
  We don't intend this introductory web page to be a complete UML tutorial, so we're not going to list any details of the different diagram types here. 
To learn more, you can check out one of the many on-line tutorials, or buy a book. (The last time we checked, typing "UML" into the search box for the major on-line booksellers returned a list of more than 100  titles!) Or, if you're technical and want the whole story, you can download the UML specification itself from the OMG website. 
It's free, of course, but it's also highly technical, terse, and very difficult for beginners to understand. 

I'M ABOUT TO START MY FIRST UML-BASED DEVELOPMENT PROJECT. WHAT DO I NEED TO DO?
Three things, probably (but not necessarily) in this order:
1)Select a methodology: A methodology formally defines the process that you use to gather requirements, analyze them, and design an application that meets them in every way. 
>>There are many methodologies, each differing in some way or ways from the others. 
>>There are many reasons why one methodology may be better than another for your particular project: For example, some are better suited for large enterprise applications while others are built to design small embedded or safety-critical systems. 
>>On another axis, some methods better support large numbers of architects and designers working on the same project, while others work better when used by one person or a small group
>>OMG, as a vendor-neutral organization, does not have an opinion about any methodology.

2)Select a UML Development Tool: Because most (although not all) UML-based tools implement a particular methodology, in some cases it might not be practical to pick a tool and then try to use it with a methodology that it wasn't built for. (For other tool/methodology combinations, this might not be an issue, or might be easy to work around.) 
>>But, some methodologies have been implemented on multiple tools so this is not strictly a one-choice environment.
>>You may find a tool so well-suited to your application or organization that you're willing to switch methodologies in order to use it. If that's the case, go ahead - our advice to pick a methodology first is general, and may not apply to a specific project. Another possibility: You may find a methodology that you like, which isn't implemented in a tool that fits your project size, or your budget, so you have to switch. If either of these cases happens to you, try to pick an alternative methodology that doesn't differ too much from the one you preferred originally. 
>>As with methodologies, OMG doesn't have an opinion or rating of UML-based modeling tools, but we do have links to a number of lists here. These will help you get started making your choice. 
>>You may find a tool so well-suited to your application or organization that you're willing to switch methodologies in order to use it. 
>>If that's the case, go ahead - our advice to pick a methodology first is general, and may not apply to a specific project. 
>>Another possibility: You may find a methodology that you like, which isn't implemented in a tool that fits your project size, or your budget, so you have to switch. 
>>If either of these cases happens to you, try to pick an alternative methodology that doesn't differ too much from the one you preferred originally. 
>>As with methodologies, OMG doesn't have an opinion or rating of UML-based modeling tools, but we do have links to a number of lists here. 
>>These will help you get started making your choice.

3)Get Training: You and your staff (unless you're lucky enough to hire UML-experienced architects) will need training in UML. 
It's best to get training that teaches how to use your chosen tool with your chosen methodology, typically provided by either the tool supplier or methodologist. 
If you decide not to go this route, check out OMG's training page for a course that meets your needs. Once you've learned UML, you can become an OMG-certified UML Professional-check here for details.
As with methodologies, OMG doesn't have an opinion or rating of UML-based modeling tools, but we do have links to a number of lists here. 
These will help you get started making your choice. 

UML 2.0 - A MAJOR UPGRADE:
The "Available" version of the UML 2.0 Superstructure specification (that is, the version that has finished its first maintenance release and been built into vendor products) has been completed, and is available to everyone for free download. 
Three separate parts of UML 2.0 - the Infrastructure (that is, the meta-metamodel), Object Constraint Language, and Diagram Interchange - are still undergoing their first maintenance and will become Available Specifications when this completes. 
There's a description of the current state of all four specifications, and links to all of them, here. 

WHAT'S NEW IN UML 2.0
We've already integrated the new features into this writeup, but here's a summary: 
1)Nested Classifiers: This is an extremely powerful concept. In UML, almost every model building block you work with (classes, objects, components, behaviors such as activities and state machines, and more) is a classifier. 
In UML 2.0, you can nest a set of classes inside the component that manages them, or embed a behavior (such as a state machine) inside the class or component that implements it. 
This capability also lets you build up complex behaviors from simpler ones, the capability that defines the Interaction Overview Diagram. 
You can layer different levels of abstraction in multiple ways: For example, you can build a model of your Enterprise, and zoom in to embedded site views, and then to departmental views within the site, and then to applications within a department. 
Alternatively, you can nest computational models within a business process model. 
OMG's Business Enterprise Integration Domain Task Force (BEI DTF) is currently working on several interesting new standards in business process and business rules. 
2)Improved Behavioral Modeling: In UML 1.X, the different behavioral models were independent, but in UML 2.0, they all derive from a fundamental definition of a behavior (except for the Use Case, which is subtly different but still participates in the new organization). 
3)Improved relationship between Structural and Behavioral Models: As we pointed out under Nested Classifiers, UML 2.0 lets you designate that a behavior represented by (for example) a State Machine or Sequence Diagram is the behavior of a class or a component. 

List of UML Diaagrams:
1)Activity Diagram.
2)Class Diagram.
3)Communication Diagram.
4)Component Diagram.
5)Deployment Diagram.
6)Object Diagram.
7)Package Diagram.
8)Sequence Diagram.
9)state Diagram.
10)Use Case Diagram.

Refering styles:

Different styles of writing reference:
1)Harvard style of referencing.
2)American Psychological Association style (APA) .
3)Vancouver style.
4)MLA citation style (modern language association).
5)The Chicago manual of style .
6)Royal society of chemistry style.

Harvard citation format:
Harvard is a style of referencing, primarily used by university students, to cite information sources.
In-text citations are used when directly quoting or paraphrasing a source.
They are located in the body of the work and contain a fragment of the full citation.
Parenthetical referencing also known as Harvard referencing,is a citation style in which partial citations.
>>for example, "(Smith 2010, p. 1)"—are enclosed within parentheses and embedded in the text, either within or after a sentence.
They are accompanied by a full, alphabetized list of citations in an end section, usually titled "references", "reference list", "works cited", or "end-text citations".

There are two styles of parenthetical referencing:
Author–date: primarily used in the sciences and social sciences, and recommended by the American Chemical Society and the American Psychological Association (APA);
Author–title or author–page: primarily used in the arts and the humanities, and recommended by the Modern Language Association (MLA).

Author–Date:
In the author–date method (Harvard referencing), the in-text citation is placed in parentheses after the sentence or part thereof that the citation supports. 
The citation includes the author's name, year of publication, and page number(s) when a specific part of the source is referred to (Smith 2008, p. 1) or (Smith 2008:1). A full citation is given in the references section: Smith, John (2008). Name of Book. Name of Publisher.

How to cite:
The structure of a citation under the author–date method is the author's surname, year of publication, and page number or range, in parentheses, as illustrated in the Smith example near the top of this article.

1)The page number or page range is omitted if the entire work is cited. The author's surname is omitted if it appears in the text. Thus we may say: "Jones (2001) revolutionized the field of trauma surgery."
2)Two authors are cited using "and" or "&": (Deane and Jones 1991) or (Deane & Jones 1991). More than two authors are cited using "et al.": (Smith et al. 1992).
3)In some documentation systems (e.g., MLA style), an unknown date is cited as having "no date of publication" by the abbreviation for "no date" (Deane, n.d.).[6]
4)In such documentation systems, works without pagination are referred to in the References list as "not paginated" with the abbreviation for that phrase (n. pag.).[6]
5)"No place of publication" and/or "no publisher" are both designated the same way (n.p.) and placed in the appropriate spot in the bibliographical citation (Harvard Referencing. N.p.).[6]
6)A reference to a republished work is cited with the original publication date either in square brackets (Marx [1867] 1967, p. 90) or separated with a slash (Marx, 1867/1967, p. 90).[7] The inclusion of the original publication year qualifies the suggestion otherwise that the publication originally occurred in 1967.
7)If an author published several books in 2005, the year of the first publication (in the alphabetic order of the references) is cited and referenced as 2005a, the second as 2005b and so on.
8)A citation is placed wherever appropriate in or after the sentence. If it is at the end of a sentence, it is placed before the period, but a citation for an entire block quote immediately follows the period at the end of the block since the citation is not an actual part of the quotation itself.
9)Complete citations are provided in alphabetical order in a section following the text, usually designated as "Works cited" or "References." The difference between a "works cited" or "references" list and a bibliography is that a bibliography may include works not directly cited in the text.
10)All citations are in the same font as the main text.
11)Note that "[t]he 'Harvard System' is something of a misnomer, as there is no official institutional connection. It's another name for the author/date citation system, the custom of using author and date in parentheses, e.g. (Robbins 1987) to refer readers to the full bibliographic citations in appended bibliographies. Some Harvard faculty were among the first practitioners in the late 19th century, and the name stuck, particularly in England and the Commonwealth countries."[8]
12)Also note that there is no official guide to Harvard citation style,[9] consequently variations occur across various online Harvard citation and referencing guides. For example, some universities instruct students to type a book's publication date without parentheses in the reference list

Examples:
An example of a journal reference:
Heilman, J. M. and West, A. G. (2015). Wikipedia and Medicine: Quantifying Readership, Editors, and the Significance of Natural Language. Journal of Medical Internet Research, 17(3), p.e62. doi:10.2196/jmir.4069.

Following is an explanation of the components, where the information in brackets is for demonstration purposes and is not used in actual formatting:
[Heilman, J. M. and West, A. G]. (2015). [Wikipedia and Medicine: Quantifying Readership, Editors, and the Significance of Natural Language]. [Journal of Medical Internet Research], [17] [(3)], [p.e62]. [doi:10.2196/jmir.4069].

[Author(s)] first listed author's name inverted in the bibliography entry
[Year]
Article title
[Journal title] in italic type
[Volume]
[Issue]
[Page numbers] specific page number in a note; page range in a bibliography entry
[Digital object identifier]

Examples of book references are:

Smith, J. (2005a). Dutch Citing Practices. The Hague: Holland Research Foundation.
Smith, J. (2005b). Harvard Referencing. London: Jolly Good Publishing.

In giving the city of publication, an internationally well-known city (such as London, The Hague, or New York) is given as the city alone. If the city is not internationally well known, the country (or state and country if in the U.S.) is given.
An example of a newspaper reference:
Bowcott, Owen (October 18, 2005). "Protests halt online auction to shoot stag", The Guardian.

Advantages:
1)The principal advantage of the author–date method is that a reader familiar with a field is likely to recognize a citation without having to check in the references section. This is most useful in fields whose works are commonly known by their date of publication (for example, the sciences and social sciences in which one cites, say, "the 2005 Johns Hopkins study of brain function"), or if the author cited is notorious (for example, HIV denialist Peter Duesberg on the cause of AIDS).
2)The use of author–date systems helps the reader easily identify sources that may be outdated.
3)If the same source is cited more than once, even a reader unfamiliar with the author may remember the name. It quickly becomes obvious if the publication is relying heavily on a single author or single publication. When many different pages of the same work are cited, the reader does not need to flip back and forth to footnotes or endnotes full of "ibid." citations to discover this fact.
4)With the author–date method, there is no renumbering hassle when the order of in-text citations is changed, which can be a scourge of the numbered endnotes system if house style or project style insists that citations never appear out of numerical order. (Computerized reference-management software automates this aspect of the numbered system [for example, Microsoft Word's endnote system, Wikipedia's <ref> system, LaTeX/BibTeX, or various applications marketed to professionals].)
5)Parenthetical referencing works well in combination with substantive notes. When the note system is used for source citations, two different systems of note marking and placement are needed—in Chicago Style, for instance, "the citation notes should be numbered and appear as endnotes. The substantive notes, indicated by asterisks and other symbols, appear as footnotes" ("Chicago Manual of Style" 2003, 16.63-64). This approach can be cumbersome in any circumstances. When it is not possible to use footnotes altogether probably because of the publisher's policy, it results in two parallel series of endnotes, which can be confusing to readers. Using parenthetical referencing for sources avoids such a problem.

Advantages:
The principal advantage of the author–date method is that a reader familiar with a field is likely to recognize a citation without having to check in the references section. This is most useful in fields whose works are commonly known by their date of publication (for example, the sciences and social sciences in which one cites, say, "the 2005 Johns Hopkins study of brain function"), or if the author cited is notorious (for example, HIV denialist Peter Duesberg on the cause of AIDS).
The use of author–date systems helps the reader easily identify sources that may be outdated.
If the same source is cited more than once, even a reader unfamiliar with the author may remember the name. It quickly becomes obvious if the publication is relying heavily on a single author or single publication. When many different pages of the same work are cited, the reader does not need to flip back and forth to footnotes or endnotes full of "ibid." citations to discover this fact.
With the author–date method, there is no renumbering hassle when the order of in-text citations is changed, which can be a scourge of the numbered endnotes system if house style or project style insists that citations never appear out of numerical order. (Computerized reference-management software automates this aspect of the numbered system [for example, Microsoft Word's endnote system, Wikipedia's <ref> system, LaTeX/BibTeX, or various applications marketed to professionals].)
Parenthetical referencing works well in combination with substantive notes. When the note system is used for source citations, two different systems of note marking and placement are needed—in Chicago Style, for instance, "the citation notes should be numbered and appear as endnotes. The substantive notes, indicated by asterisks and other symbols, appear as footnotes" ("Chicago Manual of Style" 2003, 16.63-64). This approach can be cumbersome in any circumstances. When it is not possible to use footnotes altogether probably because of the publisher's policy, it results in two parallel series of endnotes, which can be confusing to readers. Using parenthetical referencing for sources avoids such a problem

Disadvantages:
1)The principal disadvantage of parenthetical references is they take up space in the main body of the text and are distracting to a reader, especially when many works are cited in a single place (which often occurs when reviewing a large body of previous work). Numbered footnotes or endnotes, by contrast, can be combined into a range, e.g. "[27–35]". However this disadvantage is offset by the fact that parenthetical referencing may be economical for the overall document since, for instance, "(Smith 2008: 34)" takes up a small amount of space in a paragraph, whereas the same information would require a whole line in a footnote or endnote.
2)In many disciplines in the arts and humanities, date of publication is often not the most important piece of information about a particular work. Thus, in author–date references such as "(Dickens 2003: 10)", the date is essentially redundant or meaningless when read on the page, since works may go through numerous editions or translations long after the original publication. Compare a reference in a science discipline such as "The last survey indicated that four hundred were left in the wild (Jones et al. 2003)", where the date is meaningful. The reader of certain forms of arts and humanities scholarship may thus be better aided by the use of author–title referencing styles such as MLA: for example, "(Dickens Oliver, 10)", where meaningful information is given on the page. Historical scholarship is an exception, since, when citing a primary source, date of publication is meaningful, though in most branches of history footnotes are preferred on other grounds. Generally speaking, however, it is instructive that author–date systems such as Harvard were devised by scientists, whereas author–title systems such as MLA were devised by humanities scholars.
3)Similarly, because works are frequently reprinted in many arts and humanities disciplines, different author–date references might refer to the same work. For example, "(Spivak 1985)", "(Spivak 1987)", and "(Spivak 1996)" might all refer to the same essay — and might be better rendered in author–title style as "(Spivak 'Subaltern')". Such ambiguities may be resolved by adding an original date of publication, for example, "(Spivak 1985/1996)", though this is cumbersome and exacerbates the principal disadvantage of parenthetical referencing, namely its distraction for the reader and unattractiveness on the page.
4)Rules can be complicated or unclear for non-academic references, particularly those where the personal author is unknown, such as government-issued documents and standards.
5)When removing a portion of text which has citations in it, the editor(s) must also check the Reference sections to see if the sources cited in the removed text is used elsewhere in the paper or book, and if not, to delete any reference not actually cited in the text (although this issue can be eliminated by the use of reference manager software).
6)The use of the author–date methods (but not author–title) can be confusing when used in monographs about particularly prolific authors. In-text citation and back-of-the-book listings of works arranged by date of publication are conducive to errors and confusion: for example, Harvey 1996a, Harvey 1996b, Harvey 1996c, Harvey 1996d, Harvey 1995a, Harvey 1995b, Harvey 1986a, Harvey 1986b, and so on.
7)The mixing of text with frequent parentheses and long strings of numbers is typographically inelegant.
8)Most historical journals (apart from economic and social history) use footnotes because of the need for maximum flexibility. Primary source references to archives, etc., involve long and complex information, all of which may be immediately relevant to a serious reader. An interesting example of this arose with the famous work of the anthropologists John and Jean Comaroff, Of Revelation and Revolution which treated historical events from anthropological perspective: although parenthetical references were used for scholarly sources, the authors found it necessary to use notes for the historical archive material they were also using.

Author–title:
In the author–title or author–page method, also referred to as MLA style, the in-text citation is placed in parentheses after the sentence or part thereof that the citation supports, and includes the author's name (a short title only is necessary when there is more than one work by the same author) and a page number where appropriate (Smith 1) or (Smith, Playing 1). (No "p." or "pp." prefaces the page numbers and main words in titles appear in capital letters, following MLA style guidelines.) A full citation is given in the references section.

Cite the following information:
1)author(s) name and initials
2)title of the article (between single quotation marks)
3)title of the journal (in italics)
4)available publication information (volume number, issue number)
5)accessed day month year (the date you last viewed the article)
6)URL or Internet address (between pointed brackets) 


Vancouver style:

1)Author Surname followed by Initials. 
2)Title of article followed by double quotation.
3)Title of journal (abbreviated).
4)Date of Publication followed by double quotation.
5)Volume Number.
6)Issue Number in bracket.
7)Page Number.
Example:
Haas AN, Susin C, Albandar JM, et al. Azithromycin as a adjunctive treatment of aggressive periodontitis: 12-months randomized clinical trial. N Engl J Med. 2008 Aug; 35(8):696-704.
Vancouver Style does not use the full journal name, only the commonly-used abbreviation: “New England Journal of Medicine” is cited as “N Engl J Med”.   


MLA citation style (modern language association)

 1)Authors name.
 2)Title of article. 
 3)Name of journal.
 4)Volume number followed by decimal & issue no. 
 5)Year of publication.
 6)Page numbers. 
 7)Medium of publication.

Example:
Matarrita-Cascante, David. "Beyond Growth: Reaching Tourism-Led Development." Annals of Tourism Research 37.4 (2010): 1141-63. 

American Psychological Association style (APA):
 
Author’s name followed by its initials.
Year of publication.
Article title followed by full stop.
Name of Journal in italic form
Volume followed by a comma
Page no.
>>Example:
Alibali, M. W., Phillips, K. M., & Fischer, A. D. (2009). Learning new problem-solving strategies leads to changes in problem representation. Cognitive Development, 24, 89-101.

The Chicago manual of style :
1)Name of author.
2)Article title in double quotation mark.
3)Title of journal in italic.
4)Volume.
5)Year of publication.
6)Page no.
>>Example:
Joshua I. Weinstein, “The Market in Plato’s ” Classical Philology, 104 (2009): 440.
 
Royal society of chemistry style:
1)INITIALS. Author’s surname.
2)Title of journal (abbreviated).
3)Year of publication. 
4)Volume number.
5)Pages no.
>>Example:
H. Yano, K. Abe, M. Nogi, A. N. Nakagaito, J. Mater. Sci., 2010, 45, 1–33.



Extracting Information from Text:

For any given question, it's likely that someone has written the answer down somewhere. The amount of natural language text that is available in electronic form is truly staggering, and is increasing every day. 
However, the complexity of natural language can make it very difficult to access the information in that text. The state of the art in NLP is still a long way from being able to build general-purpose representations of meaning from unrestricted text. 
If we instead focus our efforts on a limited set of questions or "entity relations," such as "where are different facilities located," or "who is employed by what company," we can make significant progress.
The goal of this chapter is to answer the following questions:

1)How can we build a system that extracts structured data, such as tables, from unstructured text?
2)What are some robust methods for identifying the entities and relationships described in a text?
3)Which corpora are appropriate for this work, and how do we use them for training and evaluating our models?

Along the way, we'll apply techniques from the last two chapters to the problems of chunking and named-entity recognition.

Extracting Text from PDF, MSWord, and Other Binary Formats:

ASCII text and HTML text are human-readable formats. Text often comes in binary formats—such as PDF and MSWord—that can only be opened using specialized software.
Third-party libraries such as pypdf and pywin32 provide access to these formats.
Extracting text from multicolumn documents is particularly challenging. 
For one-off conversion of a few documents, it is simpler to open the document with a suitable application, then save it as text to your local drive, and access it as described below. 
If the document is already on the Web, you can enter its URL in Google’s search box.
The search result often includes a link to an HTML version of the document, which you can save as text.

Text Wrapping:
When the output of our program is text-like, instead of tabular, it will usually be necessary
to wrap it so that it can be displayed conveniently. Consider the following output,
which overflows its line, and which uses a complicated print statement:
>>> saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
>>> for word in saying:  print word, '(' + str(len(word)) + '),',


We can take care of line wrapping with the help of Python’s textwrap module. 
For  maximum clarity we will separate each step onto its own line:
>>> from textwrap import fill
>>> format = '%s (%d),'
>>> pieces = [format % (word, len(word)) for word in saying]
>>> output = ' '.join(pieces)
>>> wrapped = fill(output)
>>> print wrapped
After (5), all (3), is (2), said (4), and (3), done (4), , (1), more
(4), is (2), said (4), than (4), done (4), . (1),
Notice that there is a linebreak between more and its following number. If we wanted to avoid this, we could redefine the formatting string so that it contained no spaces
(e.g., '%s_(%d),'), then instead of printing the value of wrapped, we could print wrapped.replace('_', ' ').

Information Extraction:
Information comes in many shapes and sizes. One important form is structured data, where there is a regular and predictable organization of entities and relationships. 
For example, we might be interested in the relation between companies and locations. Given a particular company, we would like to be able to identify the locations where it does business; conversely, given a location, we would like to discover which companies do business in that location. 
If our data is in tabular form, such as the example in 1.1, then answering these queries is straightforward.

Table 1.1
Locations data
OrgName	                LocationName
Omnicom	                New York
DDB Needham             New York
Kaplan Thaler Group	New York
BBDO South	        Atlanta
Georgia-Pacific	        Atlanta

If this location data was stored in Python as a list of tuples (entity, relation, entity), then the question "Which organizations operate in Atlanta?" could be translated as follows:
>>> locs = [('Omnicom', 'IN', 'New York'),
...         ('DDB Needham', 'IN', 'New York'),
...         ('Kaplan Thaler Group', 'IN', 'New York'),
...         ('BBDO South', 'IN', 'Atlanta'),
...         ('Georgia-Pacific', 'IN', 'Atlanta')]
>>> query = [e1 for (e1, rel, e2) in locs if e2=='Atlanta']
>>> print(query)
['BBDO South', 'Georgia-Pacific']
Things are more tricky if we try to get similar information out of text.
For example, consider the following snippet (from nltk.corpus.ieer, for fileid NYT19980315.0085).

If you read through information extraction, you will glean the information required to answer the example question. But how do we get a machine to understand enough about information extraction to return the answers in 1.2? This is obviously a much harder task. Unlike 1.1, information extraction  contains no structure that links organization names with location names.
One approach to this problem involves building a very general representation of meaning. 
In this chapter we take a different approach, deciding in advance that we will only look for very specific kinds of information in text, such as the relation between organizations and locations. Rather than trying to use text like information extraction  to answer the question directly, we first convert the unstructured data of natural language sentences into the structured data of  Information Extraction Architecture. 
Then we reap the benefits of powerful query tools such as SQL. 
This method of getting meaning from text is called Information Extraction.

Information Extraction has many applications, including business intelligence, resume harvesting, media analysis, sentiment detection, patent search, and email scanning. A particularly important area of current research involves the attempt to extract structured data out of electronically-available scientific literature, especially in the domain of biology and medicine.

Information Extraction Architecture:
shows the architecture for a simple information extraction system. It begins by processing a document using several of the procedures discussed in 3 and 5.: first, the raw text of the document is split into sentences using a sentence segmenter, and each sentence is further subdivided into words using a tokenizer. 
Next, each sentence is tagged with part-of-speech tags, which will prove very helpful in the next step, named entity detection. 
In this step, we search for mentions of potentially interesting entities in each sentence. 
Finally, we use relation detection to search for likely relations between different entities in the text.
To perform the first three tasks, we can define a simple function that simply connects together NLTK's default sentence segmenter [1], word tokenizer [2], and part-of-speech tagger [3]:
>>> def ie_preprocess(document):
...    sentences = nltk.sent_tokenize(document) [1]
...    sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
...    sentences = [nltk.pos_tag(sent) for sent in sentences] [3]
Next, in named entity detection, we segment and label the entities that might participate in interesting relations with one another. Typically, these will be definite noun phrases such as the knights who say "ni", or proper names such as Monty Python. In some tasks it is useful to also consider indefinite nouns or noun chunks, such as every student or cats, and these do not necessarily refer to entities in the same way as definite NPs and proper names.

Finally, in relation extraction, we search for specific patterns between pairs of entities that occur near one another in the text, and use those patterns to build tuples recording the relationships between the entities.


>>Chunking
The basic technique we will use for entity detection is chunking, which segments and labels multi-token sequences as illustrated in Noun Phrase Chunking. The smaller boxes show the word-level tokenization and part-of-speech tagging, while the large boxes show higher-level chunking. Each of these larger boxes is called a chunk. Like tokenization, which omits whitespace, chunking usually selects a subset of the tokens. 
Also like tokenization, the pieces produced by a chunker do not overlap in the source text.
 Noun Phrase Chunking:
We will begin by considering the task of noun phrase chunking, or NP-chunking, where we search for chunks corresponding to individual noun phrases. For example, here is some Wall Street Journal text with NP-chunks marked using brackets:
	[ The/DT market/NN ] for/IN [ system-management/NN software/NN ] for/IN [ Digital/NNP ] [ 's/POS hardware/NN ] is/VBZ fragmented/JJ enough/RB that/IN [ a/DT giant/NN ] such/JJ as/IN [ Computer/NNP Associates/NNPS ] should/MD do/VB well/RB there/RB]
As we can see, NP-chunks are often smaller pieces than complete noun phrases. For example, the market for system-management software for Digital's hardware is a single noun phrase (containing two nested noun phrases), but it is captured in NP-chunks by the simpler chunk the market. One of the motivations for this difference is that NP-chunks are defined so as not to contain other NP-chunks. Consequently, any prepositional phrases or subordinate clauses that modify a nominal will not be included in the corresponding NP-chunk, since they almost certainly contain further noun phrases.

One of the most useful sources of information for NP-chunking is part-of-speech tags. This is one of the motivations for performing part-of-speech tagging in our information extraction system. 
We demonstrate this approach using an example sentence that has been part-of-speech tagged in Tag patterns. In order to create an NP-chunker, we will first define a chunk grammar, consisting of rules that indicate how sentences should be chunked. In this case, we will define a simple grammar with a single regular-expression rule chunking. 
This rule says that an NP chunk should be formed whenever the chunker finds an optional determiner (DT) followed by any number of adjectives (JJ) and then a noun (NN). Using this grammar, we create a chunk parser [3], and test it on our example sentence [4]. The result is a tree, which we can either print [5], or display graphically [6].

 	
>>> sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), [1]
... ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

>>> grammar = "NP: {<DT>?<JJ>*<NN>}" [2]

>>> cp = nltk.RegexpParser(grammar) [3]
>>> result = cp.parse(sentence) [4]
>>> print(result) [5]
(S
  (NP the/DT little/JJ yellow/JJ dog/NN)
  barked/VBD
  at/IN
  (NP the/DT cat/NN))
>>> result.draw() [6]


>>Tag Patterns:
 The rules that make up a chunk grammar use tag patterns to describe sequences of tagged words. A tag pattern is a sequence of part-of-speech tags delimited using angle brackets, e.g. <DT>?<JJ>*<NN>. Tag patterns are similar to regular expression patterns (3.4). Now, consider the following noun phrases from the Wall Street Journal:
    another/DT sharp/JJ dive/NN
    trade/NN figures/NNS
    any/DT new/JJ policy/NN measures/NNS
    earlier/JJR stages/NNS
    Panamanian/JJ dictator/NN Manuel/NNP Noriega/NNP
 We can match these noun phrases using a slight refinement of the first tag pattern above, i.e. <DT>?<JJ.*>*<NN.*>+. This will chunk any sequence of tokens beginning with an optional determiner, followed by zero or more adjectives of any type (including relative adjectives like earlier/JJR), followed by one or more nouns of any type. However, it is easy to find many more complicated examples which this rule will not cover:
    his/PRP$ Mansion/NNP House/NNP speech/NN
    the/DT price/NN cutting/VBG
    3/CD %/NN to/TO 4/CD %/NN
    more/JJR than/IN 10/CD %/NN
    the/DT fastest/JJS developing/VBG trends/NNS
    's/POS skill/NN

Chunking with Regular Expressions:
To find the chunk structure for a given sentence, the RegexpParser chunker begins with a flat structure in which no tokens are chunked. The chunking rules are applied in turn, successively updating the chunk structure. Once all of the rules have been invoked, the resulting chunk structure is returned.
Chunking with Regular Expressions  shows a simple chunk grammar consisting of two rules. The first rule matches an optional determiner or possessive pronoun, zero or more adjectives, then a noun. The second rule matches one or more proper nouns. We also define an example sentence to be chunked [1], and run the chunker on this input [2].
   grammar = r"""
       NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
           {<NNP>+}                # chunk sequences of proper nouns
   """
   cp = nltk.RegexpParser(grammar)
   sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), [1]
                    ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]

    >>> print(cp.parse(sentence)) [2]
    (S
      (NP Rapunzel/NNP)
      let/VBD
      down/RP
      (NP her/PP$ long/JJ golden/JJ hair/NN))
If a tag pattern matches at overlapping locations, the leftmost match takes precedence. For example, if we apply a rule that matches two consecutive nouns to a text containing three consecutive nouns, then only the first two nouns will be chunked:
    >>> nouns = [("money", "NN"), ("market", "NN"), ("fund", "NN")]
    >>> grammar = "NP: {<NN><NN>}  # Chunk two consecutive nouns"
    >>> cp = nltk.RegexpParser(grammar)
    >>> print(cp.parse(nouns))
     (S (NP money/NN market/NN) fund/NN)
Once we have created the chunk for money market, we have removed the context that would have permitted fund to be included in a chunk. This issue would have been avoided with a more permissive chunk rule, e.g.  NP: {<NN>+}.

Exploring Text Corpora:
In chunking we saw how we could interrogate a tagged corpus to extract phrases matching a particular sequence of part-of-speech tags. We can do the same work more easily with a chunker, as follows:
>>> cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
>>> brown = nltk.corpus.brown
>>> for sent in brown.tagged_sents():
...     tree = cp.parse(sent)
...     for subtree in tree.subtrees():
...         if subtree.label() == 'CHUNK': print(subtree)


Chinking:
Sometimes it is easier to define what we want to exclude from a chunk. We can define a chink to be a sequence of tokens that is not included in a chunk. In the following example, barked/VBD at/IN is a chink:
	[ the/DT little/JJ yellow/JJ dog/NN ] barked/VBD at/IN [ the/DT cat/NN ]

Chinking is the process of removing a sequence of tokens from a chunk. If the matching sequence of tokens spans an entire chunk, then the whole chunk is removed; if the sequence of tokens appears in the middle of the chunk, these tokens are removed, leaving two chunks where there was only one before. 
If the sequence is at the periphery of the chunk, these tokens are removed, and a smaller chunk remains. These three possibilities are illustrated in  Noun Phrase Chunking.

Three chinking rules applied to the same chunk
::::::    	Entire chunk	              Middle of a chunk          	End of a chunk
Input	   [a/DT little/JJ dog/NN]	 [a/DT little/JJ dog/NN]	  [a/DT little/JJ dog/NN]
Operation	Chink "DT JJ NN"	        Chink "JJ"	               Chink "NN"
Pattern	           }DT JJ NN{	   	           }JJ{	                          }NN{
Output	    a/DT little/JJ dog/NN	 [a/DT] little/JJ [dog/NN]	  [a/DT little/JJ] dog/NN

we put the entire sentence into a single chunk, then excise the chinks.


Summary:

>>>Information extraction systems search large bodies of unrestricted text for specific types of entities and relations, and use them to populate well-organized databases. These databases can then be used to find answers for specific questions.
>>>The typical architecture for an information extraction system begins by segmenting, tokenizing, and part-of-speech tagging the text.
>>>The resulting data is then searched for specific types of entity. Finally, the information extraction system looks at entities that are mentioned near one another in the text, and tries to determine whether specific relationships hold between those entities.
>>>Entity recognition is often performed using chunkers, which segment multi-token sequences, and label them with the appropriate entity type. 
>>>Common entity types include ORGANIZATION, PERSON, LOCATION, DATE, TIME, MONEY, and GPE (geo-political entity).
>>>Chunkers can be constructed using rule-based systems, such as the RegexpParser class provided by NLTK; or using machine learning techniques, such as the ConsecutiveNPChunker presented in this chapter. In either case, part-of-speech tags are often a very important feature when searching for chunks.
>>>Although chunkers are specialized to create relatively flat data structures, where no two chunks are allowed to overlap, they can be cascaded together to build nested structures.
>>>Relation extraction can be performed using either rule-based systems which typically look for specific patterns in the text that connect entities and the intervening words; or using machine-learning systems which typically attempt to learn such patterns automatically from a training corpus.

Text Similarity Approaches:
Measuring the similarity between words, sentences, paragraphs and documents is an important component in various tasks such as information retrieval, document clustering, word-sense disambiguation, automatic essay scoring, short answer grading, machine translation and text summarization. 
This survey discusses the existing works on text similarity through partitioning them into three approaches; String-based, Corpus-based and Knowledge-based similarities. 
Furthermore, samples of combination between these similarities are presented.
Text similarity measures play an increasingly important role in text related research and applications in tasks such as information retrieval, text classification, document clustering, topic detection, topic tracking, questions generation, question answering, essay scoring, short answer scoring, machine translation, text summarization and others. 
Finding similarity between words is a fundamental part of text similarity which is then used as a primary stage for sentence, paragraph and document similarities. 
Words can be similar in two ways lexically and semantically. Words are similar lexically if they have a similar character sequence. Words are similar semantically if they have the same thing, are opposite of each other, used in the same way, used in the same context and one is a type of another. 
Lexical similarity is introduced in this survey though different String-Based algorithms, Semantic similarity is introduced through Corpus-Based and Knowledge-Based algorithms. 
String-Based measures operate on string sequences and character composition. A string metric is a metric that measures similarity or dissimilarity (distance) between two text strings for approximate string matching or comparison. 
Corpus-Based similarity is a semantic similarity measure that determines the similarity between words according to information gained from large corpora. 
Knowledge-Based similarity is a semantic similarity measure that determines the degree of similarity between words using information derived from semantic networks. The most popular for each type will be presented briefly.

>>Volume of text resources have been increasing in digital libraries and internet. 
Organizing these text documents has become a practical need. 
For organizing great number of objects into small or minimum number of coherent groups automatically, Clustering technique is used. 
These documents are widely used for information retrieval and Natural Language processing tasks. 
Different Clustering algorithms require a metric for quantifying how dissimilar two given documents are. 
This difference is often measured by similarity measure such as Euclidean distance, Cosine similarity etc. The similarity measure process in text
mining can be used to identify the suitable clustering algorithm for a specific problem. 
This survey discusses the existing works on text similarity by partitioning them into three significant approaches; String-based, Knowledge based and Corpus-based similarities.

>>Document clustering is a process that involves a computational burden in measuring the similarity between document pairs. 
Similarity measure is the function which assigns a real number between  0 and 1 to the documents. 
A zero value means that the documents are dissimilar completely whereas one indicates that the documents are identical practically. 
Vector-based models have  been used for computing the similarity in document, traditionally. 
The Different features presented in the documents are represented by vector- based models.
Text similarity measures play an increasingly vital role in text related research and applications in several tasks such as text classification, information retrieval, topic tracking, document clustering,
questions generation, question answering, short answer scoring, machine translation, essay scoring, text summarization, topic detection and others.
Finding similarity between words is a necessary part of text similarity. 
It is the primary stage for sentence and document similarities. 
Words can be possibly similar in two ways lexically and semantically. 
Words are lexically similar if they have a similar character sequence. 
If the words have same theme, then they are semantically similar and if they have dissimilar theme but used in same context, then they are not related to each other. 
String-Based algorithms are used to measure Lexical similarity; Corpus-Based and Knowledge-Based algorithms are based on Semantic similarity.
String-Based measures operate on sequence of strings and composition of characters. 
For measuring the similarity and dissimilarity between the text strings, String metric is used. 
It is used for string matching or comparison but it is approximate. 

Corpus-Based Similarity:
Corpus-Based similarity is a semantic similarity measure that determines the similarity between words according to information gained from large corpora. A Corpus is a large collection of written or spoken texts that is used for language research. Figure 2 shows the Corpus-Based similarity measures.
Hyperspace Analogue to Language (HAL) [13,14] creates a semantic space from word co-occurrences. A word-by-word matrix is formed with each matrix element is the strength of association between the word represented by the row and the word represented by the column. The user of the algorithm then has the option to drop out low entropy columns from the matrix. 
As the text is analyzed, a focus word is placed at the beginning of a ten word window that records which neighboring words are counted as co-occurring. 
Matrix values are accumulated by weighting the co-occurrence inversely proportional to the distance from the focus word; closer neighboring words are thought to reflect more of the focus word's semantics and so are weighted higher. HAL also records word-ordering information by treating the co-occurrence differently based on whether the neighboring word appeared before or after the focus word.

Latent Semantic Analysis (LSA) is the most popular technique of Corpus-Based similarity. LSA assumes that words that are close in meaning will occur in similar pieces of text. A matrix containing word counts per paragraph (rows represent unique words and columns represent each paragraph) is constructed from a large piece of text and a mathematical technique which called singular value decomposition (SVD) is used to reduce the number of columns while preserving the similarity structure among rows. Words are then compared by taking the cosine of the angle between the two vectors formed by any two rows.
>>Generalized Latent Semantic Analysis (GLSA)  is a framework for computing semantically motivated term and document vectors. It extends the LSA approach by focusing on term vectors instead of the dual document-term representation. GLSA requires a measure of semantic association between terms and a method of dimensionality reduction. The GLSA approach can combine any kind of similarity measure on the space of terms with any suitable method of dimensionality reduction. The traditional term document matrix is used in the last step to provide the weights in the linear combination of term vectors.
>>Explicit Semantic Analysis (ESA) is a measure used to compute the semantic relatedness between two arbitrary texts. The Wikipedia-Based technique represents terms (or texts) as high- dimensional vectors; each vector entry presents the TF-IDF weight between the term and one Wikipedia article. 
The semantic relatedness between two terms (or texts) is expressed by the cosine measure between the corresponding vectors.
The cross-language explicit semantic analysis (CL-ESA)  is a multilingual generalization of ESA. CL-ESA exploits a document-aligned multilingual reference collection such as Wikipedia to represent a document as a language-independent concept vector. 
The relatedness of two documents in different languages is assessed by the cosine similarity between the corresponding vector representations.
>>Pointwise Mutual Information - Information Retrieval (PMI-IR)  is a method for computing the similarity between pairs of words, it uses AltaVista's Advanced Search query \ syntax to calculate probabilities.
The more often two words co-occur near each other on a web page, the higher is their PMI-IR similarity score.
>>Normalized Google Distance (NGD)  is a semantic similarity measure derived from the number of hits returned by the Google search engine for a given set of keywords. Keywords with the same or similar meanings in a natural language sense tend to be "close" in units of Google distance, while words with dissimilar meanings tend to be farther apart. 
  If the two search terms x and y never occur together on the same web page, but do occur separately, the normalized Google distance between them is infinite. If both terms always occur together, their NGD is zero, or equivalent to the coefficient between x squared and y squared.
The more often two words co-occur near each other on a web page, the higher is their PMI-IR similarity score.

>>Extracting DIStributionally similar words using CO-occurrences (DISCO)  Distributional similarity between words assumes that words with similar meaning occur in similar context. 
Large text collections are statistically analyzed to get the distributional similarity. DISCO is a method that computes distributional similarity between words by using a simple context window of size ±3 words for counting co-occurrences. 
When two words are subjected for exact similarity DISCO simply retrieves their word vectors from the indexed data, and computes the similarity according to Lin measure. 
If the most distributionally similar word is required; DISCO returns the second order word vector for the given word. 

DISCO has two main similarity measures DISCO1 and DISCO2; DISCO1 computes the first order similarity between two input words based on their collocation sets. 
DISCO2 computes the second order similarity between two input words based on their sets of distributionally similar words.

Conclusion
The  text similarity approaches is concluded  and also discussed.
Corpus-Based similarity is a semantic similarity measure that determines the similarity between words according to information gained from large corpora. 
Nine algorithms were explained; HAL, LSA, GLSA, ESA, CL-ESA, PMI-IR, SCO-PMI, NGD and DISCO.
Nine algorithms were introduced; Six of them were based on semantic similarity -res, lin, jcn, lch, wup and path- while the other three were based on semantic relatedness -hso, lesk and vector-. Some of these algorithms were combined together in many researches. Finally useful similarity packages were mentioned such as SimMetrics, WordNet::Similarity and NLTK.


References:
http://www.nltk.org/book
The popularity of chunking is due in great part to pioneering work by Abney e.g., (Church, Young, & Bloothooft, 1996). Abney's Cass chunker is described in http://www.vinartus.net/spa/97a.pdf.
The word chink initially meant a sequence of stopwords, according to a 1975 paper by Ross and Tukey (Church, Young, & Bloothooft, 1996).
The IOB format (or sometimes BIO Format) was developed for NP chunking by (Ramshaw & Marcus, 1995), and was used for the shared NP bracketing task run by the Conference on Natural Language Learning (CoNLL) in 1999. The same format was adopted by CoNLL 2000 for annotating a section of Wall Street Journal text as part of a shared task on NP chunking.


11 steps to structuring a science paper editors will take seriously:

How to Prepare a Manuscript for International Journals?
General structure of a research article
>>>title
>>>Abstract
>>>keywords
    >>Make them easy for indexing and searching!(informative, attractive, effective)
>>>Main text (IMRAD)
   >>Introduction
   >>Methods
   >>Results
   >>And
   >>Discussions
      >>Journal space is not unlimited.Make your article as concises as posible.
When you organize your manuscript, the first thing to consider is that the order of sections will be very different than the order of items on you checklist. 
An article begins with the Title, Abstract and Keywords.
The article text follows the IMRAD format(Introduction, Methods, Results, and Discussion), which responds to the questions below:
>>Introduction: What did you/others do? Why did you do it?
>>Methods: How did you do it?
>>Results: What did you find?
>>And
>>Discussion: What does it all mean?

The main text is followed by the Conclusion, Acknowledgements, References and Supporting Materials.
While this is the published structure, however, we often use a different order when writing.

Steps to organizing your manuscript
1)Prepare the figures and tables.
2)Write the Methods.
3)Write up the Results.
4)Write the Discussion. Finalize the Results and Discussion before writing the introduction. This is because, if the discussion is insufficient, how can you objectively demonstrate the scientific significance of your work in the introduction?
5)Write a clear Conclusion.
6)Write a compelling introduction.
7)Write the Abstract.
8)Compose a concise and descriptive Title.
9)elect Keywords for indexing.
10)Write the Acknowledgements.
11)Write up the References.
Next, I'll review each step in more detail. But before you set out to write a paper, there are two important things you should do that will set the groundwork for the entire process.

>>The topic to be studied should be the first issue to be solved. Define your hypothesis and objectives (These will go in the Introduction.)
>>Review the literature related to the topic and select some papers (about 30) that can be cited in your paper (These will be listed in the References.)
Finally, keep in mind that each publisher has its own style guidelines and preferences, so always consult the publisher's Guide for Authors.

Step 1: Prepare the figures and tables
Remember that "a figure is worth a thousand words." Hence, illustrations, including figures and tables, are the most efficient way to present your results. Your data are the driving force of the paper, so your illustrations are critical!
How do you decide between presenting your data as tables or figures? Generally, tables give the actual experimental results, while figures are often used for comparisons of experimental results with those of previous works, or with calculated/theoretical values.
Whatever your choice is, no illustrations should duplicate the information described elsewhere in the manuscript.

Another important factor: figure and table legends must be self-explanatory
When presenting your tables and figures, appearances count! To this end:
>>Avoid crowded plots (Figure 3), using only three or four data sets per figure; use well-selected scales.
>>Think about appropriate axis label size
>>Include clear symbols and data sets that are easy to distinguish.
>>Never include long boring tables (e.g., chemical compositions of emulsion systems or lists of species and abundances). You can include them as supplementary material.

If you are using photographs, each must have a scale marker, or scale bar, of professional quality in one corner.
In photographs and figures, use color only when necessary when submitting to a print publication. If different line styles can clarify the meaning, never use colors or other thrilling effects or you will be charged with expensive fees. 
Of course, this does not apply to online journals. For many journals, you can submit duplicate figures: one in color for the online version of the journal and pdfs, and another in black and white for the hardcopy journal.
Another common problem is the misuse of lines and histograms. Lines joining data only can be used when presenting time series or consecutive samples data. However, when there is no connection between samples or there is not a gradient, you must use histograms.

Length of the manuscript:
Again, look at the journal's Guide for Authors, but an ideal length for a manuscript is 25 to 40 pages, double spaced, including essential data only. Here are some general guidelines:
>>>Title: Short and informative
>>>Abstract: 1 paragraph(<50 words)
>>>Introduction: 1.5-2 pages
>>>Methods: 2-3 pages
>>>Results: 6-8 pages
>>>Discussion: 4-6 pages
>>>Conclusion: 1 paragraph
>>>Figures: 6-8(one per page)
>>>tables: 1-3(one per page)
>>>References: 20-50 papers(2-4 pages)

References:
https://www.elsevier.com/connect/11-steps-to-structuring-a-science-paper-editors-will-take-seriously


How to make figures for scientific papers?
To make engineering diagrams (with proper image scaling) by using  Asymptote. The learning curve is steep but image quality is very good. It also works with 3D and animations. 



What is the best software for making and editing scientific images for publication quality figures?
>> Tecplot(3D and animation)
>> Little tip
>> GraphPad 
>> Powerpoint
>> Grapher
>> Smartdraw
>> Photo/bitmap editing
>> Matlab
>> drawio

References:
https://www.Researchgate.net
https://www.publishingcampus.elsevier.com



How can you make a good presentation even more effective?

Top Tips for Effective Presentations

1.Show your Passion and Connect with your Audience

  It’s hard to be relaxed and be yourself when you’re nervous.
  But time and again, the great presenters say that the most important thing is to connect with your audience, and the best way to do that is to let your passion for the subject shine through.
  Be honest with the audience about what is important to you and why it matters.
  Be enthusiastic and honest, and the audience will respond.

2. Focus on your Audience’s Needs
  Your presentation needs to be built around what your audience is going to get out of the presentation.
  As you prepare the presentation, you always need to bear in mind what the audience needs and wants to know, not what you can tell them.
  While you’re giving the presentation, you also need to remain focused on your audience’s response, and react to that.
  You need to make it easy for your audience to understand and respond.

3. Keep it Simple: Concentrate on your Core Message
  When planning your presentation, you should always keep in mind the question:
What is the key message (or three key points) for my audience to take away?
  You should be able to communicate that key message very briefly.
  Some experts recommend a 30-second ‘elevator summary’, others that you can write it on the back of a business card, or say it in no more than 15 words.
Whichever rule you choose, the important thing is to keep your core message focused and brief.
  And if what you are planning to say doesn’t contribute to that core message, don’t say it.

4. Smile and Make Eye Contact with your Audience
  This sounds very easy, but a surprisingly large number of presenters fail to do it.
  If you smile and make eye contact, you are building rapport, which helps the audience to connect with you and your subject. It also helps you to feel less nervous, because you are talking to individuals, not to a great mass of unknown people.
  To help you with this, make sure that you don’t turn down all the lights so that only the slide screen is visible. Your audience needs to see you as well as your slides.

5. Start Strongly
  The beginning of your presentation is crucial. You need to grab your audience’s attention and hold it.
  They will give you a few minutes’ grace in which to entertain them, before they start to switch off if you’re dull. So don’t waste that on explaining who you are. Start by entertaining them.
  Try a story (see tip 7 below), or an attention-grabbing (but useful) image on a slide.

6. Remember the 10-20-30 Rule for Slideshows
  This is a tip from Guy Kawasaki of Apple. He suggests that slideshows should:
    >Contain no more than 10 slides;
    >Last no more than 20 minutes; and
    >Use a font size of no less than 30 point.
    >This last is particularly important as it stops you trying to put too much information on any one slide. This whole approach avoids the dreaded ‘Death by PowerPoint’.
  As a general rule, slides should be the sideshow to you, the presenter. A good set of slides should be no use without the presenter, and they should definitely contain less, rather than more, information, expressed simply.
  If you need to provide more information, create a bespoke handout and give it out after your presentation.


7. Tell Stories:
  Human beings are programmed to respond to stories.
  Stories help us to pay attention, and also to remember things. If you can use stories in your presentation, your audience is more likely to engage and to remember your points afterwards. It is a good idea to start with a story, but there is a wider point too: you need your presentation to act like a story.
  Think about what story you are trying to tell your audience, and create your presentation to tell it.
  >>Finding The Story Behind Your Presentation
  >>>To effectively tell a story, focus on using at least one of the two most basic storytelling mechanics in your presentation:
     1.Focusing On Characters – People have stories; things, data, and objects do not. So ask yourself “who” is directly involved in your topic that you can use as the focal point of your story.
     2.A Changing Dynamic – A story needs something to change along the way. So ask yourself “What is not as it should be?” and answer with what you are going to do about it (or what you did about it).

8. Use your Voice Effectively.
  The spoken word is actually a pretty inefficient means of communication, because it uses only one of your audience’s five senses. That’s why presenters tend to use visual aids, too. But you can help to make the spoken word better by using your voice effectively.
  Varying the speed at which you talk, and emphasising changes in pitch and tone all help to make your voice more interesting and hold your audience’s attention.
   
   Effective Speaking:
   Your voice can reveal as much about your personal history as your appearance.
   The sound of a voice and the content of speech can provide clues to an individual's emotional state and a dialect can indicate their geographic roots.   
   The voice is unique to the person to whom it belongs.

   Aspects of Effective Speaking
   Effective speaking has nothing to do with the outdated concept of 'elocution' where everyone was encouraged to speak in the same 'correct' manner.  Rather, effective speaking concerns being able to speak in a public context with confidence and clarity, whilst at the same time reflecting on your own personality
   >>Accents.
   >>Finding your voice.
   >>The effect of breath on voice and speech.
   >>Vocal production.
  
   Vocal Production:
   The following three core elements of vocal production need to be understood for anyone wishing to become an effective speaker:
   >>Volume   -  to be heard.
   >>Clarity  -  to be understood.
   >>Variety  -  to add interest.
   >>>Pace,Volume,Pitch - Inflection - Emphasis,Pause.

9. Use your Body Too
  It has been estimated that more than three quarters of communication is non-verbal.
  That means that as well as your tone of voice, your body language is crucial to getting your message across. Make sure that you are giving the right messages: body language to avoid includes crossed arms, hands held behind your back or in your pockets, and pacing the stage.
  Make your gestures open and confident, and move naturally around the stage, and among the audience too, if possible.

10. Relax, Breathe and Enjoy
  If you find presenting difficult, it can be hard to be calm and relaxed about doing it.
  One option is to start by concentrating on your breathing. Slow it down, and make sure that you’re breathing fully. Make sure that you continue to pause for breath occasionally during your presentation too.

References:
1)https://www.skillsyouneed.com/present/presentation-tips.html
2)http://acmg.seas.harvard.edu/education.html
