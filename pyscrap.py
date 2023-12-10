import json

def generate_body(position,scale,rotation,color,shapeId):
    body = {
        "bounds":{"x":scale[0],"y":scale[1],"z":scale[2]},
        "pos":{"x":position[0],"y":position[1],"z":position[2]},
        "color":color,"shapeId":shapeId,
        "xaxis":rotation[0],"zaxis":rotation[1]
    }
    return body

def create_body(position,scale,rotation,color,shapeId):
    global lastId
    lastId += 1
    body = generate_body(position,scale,rotation,color,shapeId)
    childs.append(body)
def create_logicgate(position,rotation,color,mode):
    if mode == 'AND': m = 0
    if mode == 'OR': m = 1
    if mode == 'XOR': m = 2
    if mode == 'NAND': m = 3
    if mode == 'NOR': m = 4
    if mode == 'XNOR': m = 5
    global lastId
    lastId += 1
    body = generate_body(position,[1,1,1],rotation,color,shapeIds['logic_gate'])
    body.update({'controller':{'active':False,'controllers':None,"id":lastId,"joints":None,"mode":m}})
    childs.append(body)
    return lastId-1

def connect(part1,part2):
    global childs
    if not childs[part1]['controller']['controllers']:
        childs[part1]['controller']['controllers'] = [{"id":part2+1}]
    else:
        childs[part1]['controller']['controllers'].append({"id":part2+1})

def compile(outFile):
    blueprint = {"bodies":[{"childs":childs}],"version":version}
    text = json.dumps(blueprint)
    with open(outFile,'w') as file:
        file.write(text)
def generate_ids():
    return {
        "concrete":"a6c6ce30-dd47-4587-b475-085d55c6a3b4",
        "logic_gate":"9f0f56e8-2c31-4d83-996c-d00a9b296c3f"
    }

childs = []
version = 4
lastId = 0
shapeIds = generate_ids()