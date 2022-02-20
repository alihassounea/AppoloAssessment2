

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;


import com.google.gson.JsonElement;
import com.google.gson.JsonIOException;

import com.google.gson.JsonParser;
import com.google.gson.JsonSyntaxException;

import at.uibk.dps.ee.model.graph.SpecificationProvider;
import at.uibk.dps.sc.core.ScheduleModel;
import at.uibk.dps.sc.core.scheduler.Scheduler;
import at.uibk.dps.sc.core.scheduler.SchedulerSingleOption;

import net.sf.opendse.model.Mapping;
import net.sf.opendse.model.Resource;
import net.sf.opendse.model.Task;




public class Test {
	
	static String originaltext = null;
	static int batchCount=0;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		

		ScheduleModel tested = new ScheduleModel();

	//Creating Tasks
		Task Divide = new Task("Divide");
		Task Count = new Task("Count");
		Task Sum = new Task("Sum");
		Task Clean = new Task("Clean");
		
	//Preparing Resources for AWS Serverless Functions
		
		Resource res1 = new Resource("https://6k0nzc0d4f.execute-api.us-east-1.amazonaws.com/Divide");
		Resource res2 = new Resource("https://9dpht1brp6.execute-api.us-east-1.amazonaws.com/Count");
		Resource res3 = new Resource("https://gc2ftuh5w8.execute-api.us-east-1.amazonaws.com/Sum");
		Resource res4 = new Resource("https://wajejjt7s2.execute-api.us-east-1.amazonaws.com/Clean");
		
		res1.setType("Serverless");
		res2.setType("Serverless");
		res3.setType("Serverless");
		res4.setType("Serverless");
		
		
	//Preparing Resources for Docker Local Functions
		
		Resource res1_Docker = new Resource("alihassounea/divide");
		Resource res2_Docker = new Resource("alihassounea/count");
		Resource res3_Docker = new Resource("alihassounea/sum");
		Resource res4_Docker = new Resource("alihassounea/clean");
		
		res1.setType("Local");
		res2.setType("Local");
		res3.setType("Local");
		res4.setType("Local");
		
		
	//Reading the JSON File in order to  count the number of Batches
		JsonParser parser = new JsonParser();
		try { 
		   JsonElement jsontree = parser.parse(
		       new FileReader(
		           "AssInput\\AssInput.json"
		       )
		   );
		   JsonElement je = jsontree.getAsJsonObject();
		   originaltext = je.getAsJsonObject().get("originaltext").toString();
		   String[] words = originaltext.split("\\s+");
		   batchCount = words.length/2;
		   System.out.println (originaltext);
		   System.out.println (batchCount);
		   
		
		}  
		catch (JsonIOException e) {
		   e.printStackTrace();
		} catch (JsonSyntaxException e) {
		   e.printStackTrace();
		} catch (FileNotFoundException e) {
		   e.printStackTrace();
		}
		
	//Adding Mapping in function of Batches Number
		
		Mapping<Task, Resource> mapping1, mapping2, mapping3, mapping4;
		
		
		if(batchCount>=10)
		{
		mapping1 = new Mapping<Task, Resource>("Divide", Divide, res1);
		mapping2 = new Mapping<Task, Resource>("Count", Count, res2);
		mapping3 = new Mapping<Task, Resource>("Sum", Sum, res3);
		mapping4 = new Mapping<Task, Resource>("Clean", Clean, res4);
		}
		else
		{
		mapping1 = new Mapping<Task, Resource>("Divide", Divide, res1_Docker);
		mapping2 = new Mapping<Task, Resource>("Count", Count, res2_Docker);
		mapping3 = new Mapping<Task, Resource>("Sum", Sum, res3_Docker);
		mapping4 = new Mapping<Task, Resource>("Clean", Clean, res4_Docker);
		}
		
	//Add Mappings to Schedule
		Set<Mapping<Task, Resource>> schedule = new HashSet<>();
		schedule.add(mapping1);
		schedule.add(mapping2);
		schedule.add(mapping3);
		schedule.add(mapping4);



	}

}
