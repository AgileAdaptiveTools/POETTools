
package org.mitre.poet.model.tests;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceFeature;


/**
 * This class was generated by the JAXWS SI.
 * JAX-WS RI 2.1-02/02/2007 03:56 AM(vivekp)-FCS
 * Generated source version: 2.1
 * 
 */
@WebServiceClient(name = "ModelCompilerWSService", targetNamespace = "http://ws.model.poet.mitre.org/", wsdlLocation = "http://localhost:9000/ModelCompilerWS?wsdl")
public class ModelCompilerWSService
    extends Service
{

    private final static URL MODELCOMPILERWSSERVICE_WSDL_LOCATION;

    static {
        URL url = null;
        try {
            url = new URL("http://localhost:9000/ModelCompilerWS?wsdl");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        MODELCOMPILERWSSERVICE_WSDL_LOCATION = url;
    }

    public ModelCompilerWSService(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public ModelCompilerWSService() {
        super(MODELCOMPILERWSSERVICE_WSDL_LOCATION, new QName("http://ws.model.poet.mitre.org/", "ModelCompilerWSService"));
    }

    /**
     * 
     * @return
     *     returns ModelCompilerWS
     */
    @WebEndpoint(name = "ModelCompilerWSPort")
    public ModelCompilerWS getModelCompilerWSPort() {
        return (ModelCompilerWS)super.getPort(new QName("http://ws.model.poet.mitre.org/", "ModelCompilerWSPort"), ModelCompilerWS.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns ModelCompilerWS
     */
    @WebEndpoint(name = "ModelCompilerWSPort")
    public ModelCompilerWS getModelCompilerWSPort(WebServiceFeature... features) {
        return (ModelCompilerWS)super.getPort(new QName("http://ws.model.poet.mitre.org/", "ModelCompilerWSPort"), ModelCompilerWS.class, features);
    }

}