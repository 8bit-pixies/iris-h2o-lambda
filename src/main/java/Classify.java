import org.python.util.PythonInterpreter;
import org.python.core.*;
import com.amazonaws.services.lambda.runtime.Context;
import java.util.Properties;
 
public class Classify {

  public static final class SharedPythonInterpreter {
    public static PythonInterpreter get() {
      Properties props = new Properties(System.getProperties());
      props.setProperty("python.security.respectJavaAccessibility", "false");
      PythonInterpreter.initialize(props, null, new String[0]);
      return new PythonInterpreter();
    }
  }

  public static class RequestClass {
	// what the payload looks like (inbound)
    double c0;
	double c1;
	double c2;
	double c3;

    public double getC0() { return c0; }
    public void setC0(double c0) { this.c0 = c0; }
	
    public double getC1() { return c1; }
    public void setC1(double c1) { this.c1 = c1; }
	
    public double getC2() { return c2; }
    public void setC2(double c2) { this.c2 = c2; }
	
    public double getC3() { return c3; }
    public void setC3(double c3) { this.c3 = c3; }

    public RequestClass(double c0, double c1, double c2, double c3) { 
		this.c0 = c0;
		this.c1 = c1;
		this.c2 = c2;
		this.c3 = c3;
	}

    public RequestClass() {}
  }

  public static class ResponseClass {
	// what the payload looks like (outbound)
    int label;
    double class0Prob;
    double class1Prob;
	double class2Prob;
    
    public int getLabel() { return label; }
    public void setLabel(int label) { this.label = label; }

    public double getClass0Prob() { return class0Prob; }
    public void setClass0Prob(double class0Prob) { this.class0Prob = class0Prob; }
    
    public double getClass1Prob() { return class1Prob; }
    public void setClass1Prob(double class1Prob) { this.class1Prob = class1Prob; }
	
    public double getClass2Prob() { return class1Prob; }
    public void setClass2Prob(double class2Prob) { this.class1Prob = class1Prob; }

    public ResponseClass(double[] predictions) {
      this.label = (int) predictions[0];
      this.class0Prob = predictions[1];
      this.class1Prob = predictions[2];
	  this.class2Prob = predictions[3];
    }

    public ResponseClass() {}

  }

  public static ResponseClass myHandler(RequestClass request, Context context) throws PyException {
      
    PyModule module = new PyModule();
    
    //Prediction code is in pymodule.py
    double[] predictions = module.predict(request.c0, request.c1, request.c2, request.c3);
    return new ResponseClass(predictions);
  }

  public static class PyModule {
    private PythonInterpreter interpreter = SharedPythonInterpreter.get();
    private PyFunction py_predict;

    public PyModule() {
      this.interpreter.exec("from pymodule import predict");
      this.py_predict = (PyFunction) this.interpreter.get("predict");
    }

    public double[] predict(double c0, double c1, double c2, double c3) {
      double[] predictions = new double[4]; 
      Iterable<PyObject> pyObjectIterable = py_predict.__call__(new PyFloat(c0), new PyFloat(c1), new PyFloat(c2), new PyFloat(c3)).asIterable();
      int i = 0;
      for (PyObject po : pyObjectIterable) {
         predictions[i++] = po.asDouble();
      }
      return predictions;
    }

  }
}
