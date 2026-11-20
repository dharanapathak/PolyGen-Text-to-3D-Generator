import math

def _mesh(vertices, faces, name):
    obj_lines = [f"o {name}"] + [f"v {x:.5f} {y:.5f} {z:.5f}" for x,y,z in vertices] + ["f " + " ".join(str(i+1) for i in face) for face in faces]
    return {"x":[v[0] for v in vertices], "y":[v[1] for v in vertices], "z":[v[2] for v in vertices], "i":[f[0] for f in faces], "j":[f[1] for f in faces], "k":[f[2] for f in faces], "obj":"\n".join(obj_lines), "name":name}

def cube(center=(0,0,0), size=1, name="cube"):
    cx,cy,cz=center; h=size/2
    v=[(cx-h,cy-h,cz-h),(cx+h,cy-h,cz-h),(cx+h,cy+h,cz-h),(cx-h,cy+h,cz-h),(cx-h,cy-h,cz+h),(cx+h,cy-h,cz+h),(cx+h,cy+h,cz+h),(cx-h,cy+h,cz+h)]
    f=[(0,1,2),(0,2,3),(4,6,5),(4,7,6),(0,4,5),(0,5,1),(1,5,6),(1,6,2),(2,6,7),(2,7,3),(3,7,4),(3,4,0)]
    return _mesh(v,f,name)

def sphere(center=(0,0,0), radius=0.6, rings=10, segments=16, name="sphere"):
    cx,cy,cz=center; v=[]
    for r in range(rings+1):
        phi=math.pi*r/rings
        for s in range(segments):
            theta=2*math.pi*s/segments
            v.append((cx+radius*math.sin(phi)*math.cos(theta),cy+radius*math.sin(phi)*math.sin(theta),cz+radius*math.cos(phi)))
    f=[]
    for r in range(rings):
        for s in range(segments):
            a=r*segments+s; b=r*segments+(s+1)%segments; c=(r+1)*segments+(s+1)%segments; d=(r+1)*segments+s
            if r>0: f.append((a,b,d))
            if r<rings-1: f.append((b,c,d))
    return _mesh(v,f,name)

def cylinder(center=(0,0,0), radius=0.5, height=1, segments=16, name="cylinder"):
    cx,cy,cz=center; v=[]
    for z in (cz-height/2, cz+height/2):
        for s in range(segments):
            t=2*math.pi*s/segments; v.append((cx+radius*math.cos(t),cy+radius*math.sin(t),z))
    faces=[]
    for s in range(segments):
        n=(s+1)%segments; faces.extend([(s,n,segments+n),(s,segments+n,segments+s)])
    faces.extend([(tuple(range(segments))), tuple(range(segments,2*segments))])
    # cap faces represented as triangles for Plotly/OBJ
    cap=[]
    for s in range(1,segments-1): cap.extend([(0,s,s+1),(segments,segments+s+1,segments+s)])
    faces=faces[:-2]+cap
    return _mesh(v,faces,name)

def cone(center=(0,0,0), radius=0.55, height=1.2, segments=16, name="cone"):
    cx,cy,cz=center; v=[(cx,cy,cz+height/2)]
    for s in range(segments):
        t=2*math.pi*s/segments; v.append((cx+radius*math.cos(t),cy+radius*math.sin(t),cz-height/2))
    faces=[]
    for s in range(segments): faces.append((0,s+1,(s+1)%segments+1))
    for s in range(1,segments-1): faces.append((1,s+1,s+2))
    return _mesh(v,faces,name)

def build_asset(parsed):
    shape=parsed["shape"]
    if shape=="sphere": return [sphere()]
    if shape=="cylinder": return [cylinder()]
    if shape=="cone": return [cone()]
    if shape=="robot":
        return [cube((0,0,0.45),0.65,"robot_body"), cube((0,0,1.0),0.45,"robot_head"), cube((-0.48,0,0.35),0.18,"left_arm"), cube((0.48,0,0.35),0.18,"right_arm"), cube((-0.18,0,-0.45),0.18,"left_leg"), cube((0.18,0,-0.45),0.18,"right_leg")]
    return [cube()]
