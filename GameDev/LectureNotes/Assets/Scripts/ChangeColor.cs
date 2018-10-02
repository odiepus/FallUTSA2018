using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeColor : MonoBehaviour {
    private Transform myTransform;
    public MeshRenderer sphere; 

	// Use this for initialization
	void Start () {
        myTransform = GetComponent<Transform>();
	}
	
	// Update is called once per frame
	void Update () {
        myTransform.position += new Vector3(1f * Time.deltaTime, 0, 0);
        if(myTransform.position.x > 5)
        {
            gameObject.GetComponent<MeshRenderer>().materials[0].color = Color.red;
            sphere.materials[0].color = Color.green;
        }
	}
}
