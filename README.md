<h2><i><u>Market-Basket-Analysis</></i></h2>
- Market Basket Analysis using Apriori Algorithm 

<a href = 'https://github.com/gitganeshnethi/Datasets'>Refer DataSets Repository for data which I used in above models</a>

<h3>Purpose :</h3>
<p><b>When get an oppurtunity on retail project where your problem statement is to improve store performance regarding sales and reduce store inventory, in such cases Market Basket Analysis is the technique that gives best rules.</b></p>

<ol>
<li>Market basket Analysis allows retailers to know the relationship or association between items which are more frequently bought together</li>
<li>Can be implemented using technique called Apriori Algorithm</li></ol>

<b>By looking into this example let us understand how it is done</b>

 * Imagine we have transactions of <b>n</b> customers who purchased something from retail store</li>
 * Transactions are like this... 
 <p> Customer 1: Bread, egg, papaya, oats</p>
 <p> Customer 2: Papaya, bread, oat packet and milk</p>
 <p> Customer 3: Egg, bread, and butter</p>
 <p> Customer 4: Oat packet, egg, and milk</p>
 <p> Customer 5: Milk, bread, and butter</p>
 <p> Customer 6: Papaya and milk</p>
 <p> Customer 7: Butter, papaya, and bread</p>
 <p> Customer 8: Egg and bread</p>
 <p> Customer 9: Papaya and oat packet</p>
 <p> Customer 10: Milk, papaya, and bread</p>
 <p> Customer 11: Egg and milk</p>
 <p> .             .</p>
 <p> .             .</p>
 <p> .             .</p>
 <p> Customer n    .</ul></p>
 
<b>Observe through the transactions that three customers have bought bread and butter, the technique will tell us that if bread is bought then there is high chance that same customer also bought butter.</b>
<p>Generally this technique gives best patterns for retailers to promote and cross-sell their items in store.</p>

<ol>
<p>Three metrics in finding these association rules are</p>
<li>Support</li>
<li>Confidence</li>
<li>Lift</li></ol>

<h4>Support :</h4>
<p>Support is the minimum probability for the product to get sold. Percentage of orders that contain the item set is explained</p>

<b> Support{x} = freq(x)/n </b> [x --> item, n --> total no of transactions]

  
<h4>Confidence :<h4>
<p>Given two items x,y confidence measure the percentage of times that item y is purchased, given that x was purchased</p>
<p>Confidence Value always ranges between 0 and 1. Where 0 indicates y is never purchased when x is purchased</p>
<p>1 indicates y is always purchased whenever x is purchased</p>
<b> Confidence{x,y} = freq(x,y)/freq(x)</b>
  
<h4>Lift :</h4>
<p>This is unlike confidence metric whose value may vary depending on direction</p>
Example : Confidence{x,y} is different from Confidence{y,x}
<p>Lift has no direction, which means <b>lift{x,y} = lift{y,x}</b></p>
<b>Lift{x,y} = support{x,y}/(support{x}*support{y}) </b>

<ul>
  <li>When Lift = 1; implies no relationship between x and y i.e., x and y occur together only by chance</li>
  <li>When Lift > 1; implies there is positive relationship between x and y i.e., x and y occur together more offer than random</li>
  <li>When Lift < 1; implies there is negative relationship between x and y i.e., x and y occur less often and random</li></ul>

<img src='http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1530898580/Image_1_ip8nzc.png'>
