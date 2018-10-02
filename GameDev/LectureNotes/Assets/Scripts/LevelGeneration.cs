using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LevelGeneration : MonoBehaviour {
    public GameObject baseFloor;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    void Awake()
    {
        Vector3 currentPosition = new Vector3(0, -1, 0);
        Transform trans = gameObject.GetComponent<Transform>();

        for(int i = 0; i < 10; i++)
        {
            Instantiate(baseFloor, currentPosition, trans.rotation);
            currentPosition += new Vector3(0, 0, 25f);
        }

    }
}