from Vector import vector3 as vec3
from Plane import plane as pl
from Material import color
from Material import texture as tex
import config as c
import math


class Object:
    def __init__(self,vector3=[],plane=[],type='polygon',size=0):
        self.vector3 = []
        #self.color = []
        self.plane = []
        #self.texture = tex.Texture(rfc)
        self.type = 'polygon'
        self.size = 0
    def copy(self):
        return Object(self.vector3.copy(),self.plane.copy(),self.type,self.size)
    def dot(self,v,index):
        if index < self.size & index >= 0:
            return self.vector3[index].dot(self,v)
    def addPolygon(self,x0=0,y0=0,z0=0,x1=0,y1=0,z1=0,x2=0,y2=0,z2=0,color=[0,0,0],id=""):
        self.plane.append(pl.Plane(x0,y0,z0,x1,y1,z1,x2,y2,z2,color,id))
        v0 = vec3.Vector(x0,y0,z0,x1,y1,z1)
        v1 = vec3.Vector(x2,y2,z2,x1,y1,z1)
        v0 = v0.cross(v1)
        self.vector3.append(v0)
        #self.color.append(color)
        self.size += 1
    def addSphere(self,x0,y0,z0,r0):
        t = 0
        step = c.t_step * math.pi
        td = 0
        td_step = c.td_step * math.pi

        # cord0 = co.Cord(x0,y0,z0)
        #
        # list_cord0 = []
        # list_cord0.extend(cord0)
        # print(list_cord0[0].rotate('z',step))
        # i = 0
        # while t < math.pi:
        #     print(i)
        #     new_cord0 = list_cord0[i].rotate('z',step)
        #     list_cord0.extend(new_cord0)
        #     i += 1
        #     t += step
        # list_cord1 = list_cord0.copy()
        # list_cord1 = [x.rotate('y',td_step) for x in list_cord1]
    def export(self,layer):
        print("unfinished")






#
# int * mx_toint(struct Matrix mx, int *result, int row){
# 	int i;
# 	for(i = 0;i < mx.col;i++){
# 		result[i] = round(mx_get(mx, row, i + 1));
# 	}
# 	return result;
# }
#
# //init default 4 row point matrix
# struct Matrix mx_init(struct Matrix mx, int col){
#
# 	mx.col = col;
# 	mx.type = 'a';
#
# 	mx.x = malloc (col * sizeof(double));
# 	mx.y = malloc (col * sizeof(double));
# 	mx.z = malloc (col * sizeof(double));
# 	//mx.one = malloc (col * sizeof(double));
#
# 	int i;
# 	for(i = 0; i < col; i++){
# 		mx.x[i] = INIT_VALUE;
# 		mx.y[i] = INIT_VALUE;
# 		mx.z[i] = INIT_VALUE;
# 		//mx.one[i] = 1;
# 	}
#
# 	return mx;
# }
#
# struct Matrix mx_init_e(struct Matrix mx, int col){
#
# 	mx.col = col;
# 	mx.type = 'b';
# 	mx.edge_num = 0;
#
# 	mx.x = malloc (col * sizeof(double));
# 	mx.y = malloc (col * sizeof(double));
# 	mx.z = malloc (col * sizeof(double));
# 	//mx.one = malloc (col * sizeof(double));
#
# 	int i;
# 	for(i = 0; i < col; i++){
# 		mx.x[i] = INIT_VALUE;
# 		mx.y[i] = INIT_VALUE;
# 		mx.z[i] = INIT_VALUE;
# 		//mx.one[i] = 1;
# 	}
#
# 	return mx;
# }
#
# struct Matrix mx_init_p(struct Matrix mx, int col){
# 	mx.col = col;
# 	mx.type = 'c';
# 	//mx.edge_num = 0;
#
# 	mx.x = malloc (col * sizeof(double));
# 	mx.y = malloc (col * sizeof(double));
# 	mx.z = malloc (col * sizeof(double));
# 	mx.vx = malloc (col / 3 * sizeof(double));
# 	mx.vy = malloc (col / 3 * sizeof(double));
# 	mx.vz = malloc (col / 3 * sizeof(double));
#
# 	int i;
# 	for(i = 0; i < col; i++){
# 		mx.x[i] = INIT_VALUE;
# 		mx.y[i] = INIT_VALUE;
# 		mx.z[i] = INIT_VALUE;
#
# 		//mx.one[i] = 1;
# 	}
#
# for(i = 0; i < col / 3; i++){
# 	mx.vx[i] = INIT_VALUE;
# 	mx.vy[i] = INIT_VALUE;
# 	mx.vz[i] = INIT_VALUE;
# }
#
# 	return mx;
# }
#
# struct Matrix mx_addmatrix(struct Matrix src, struct Matrix dst){
# 	if(src.type == 'a' && dst.type == 'a'){
# 		int lim = dst.col + src.col;
# 		int size = lim * sizeof(double);
#
# 		dst.x = (double *)realloc(dst.x, size);
# 		dst.y = (double *)realloc(dst.y, size);
# 		dst.z = (double *)realloc(dst.z, size);
#
# 		int i;
# 		int j = 0;
#
# 		for(i = dst.col; i < lim; i++){
# 			dst.x[i] = src.x[j];
# 			dst.y[i] = src.y[j];
# 			dst.z[i] = src.z[j];
# 			j++;
# 		}
#
# 		dst.col = lim;
# 		return dst;
# 	}else if(src.type == 'c' && dst.type == 'c'){
# 		int lim = dst.col + src.col;
# 		int size = lim * sizeof(double);
# 		int vlim = dst.col / 3 + src.col / 3;
# 		int vsize = vlim * sizeof(double);
#
# 		dst.x = (double *)realloc(dst.x, size);
# 		dst.y = (double *)realloc(dst.y, size);
# 		dst.z = (double *)realloc(dst.z, size);
#
# 		dst.vx = (double *)realloc(dst.vx, vsize);
# 		dst.vy = (double *)realloc(dst.vy, vsize);
# 		dst.vz = (double *)realloc(dst.vz, vsize);
#
# 		int i;
# 		int j = 0;
#
# 		for(i = dst.col; i < lim; i++){
# 			dst.x[i] = src.x[j];
# 			dst.y[i] = src.y[j];
# 			dst.z[i] = src.z[j];
# 			j++;
# 		}
#
# 		j = 0;
#
# 		for(i = dst.col / 3; i < vlim; i++){
# 			dst.vx[i] = src.vx[j];
# 			dst.vy[i] = src.vy[j];
# 			dst.vz[i] = src.vz[j];
# 			j++;
# 		}
#
# 		dst.col = lim;
# 		return dst;
#
# 	}else{
# 		printf("Error: mx_addmatrix, inconsistent matrix type or matrix type not supported\n");
# 	}
# }
#
# //actual math input
# double mx_get(struct Matrix mx, int row, int col){
#  	if(row == 0 || col == 0){
#  		printf("Error: mx_get array start with 1\n");
#  	}else if(row == 1){
#  		return mx.x[col - 1];
#  	}else if(row == 2){
#  		return mx.y[col - 1];
#  	}else if(row == 3){
#  		return mx.z[col - 1];
#  	}else if(row == 4){
# 		//return mx.one[col - 1];
#  	}else{
#  		printf("Err: mx_get, invalid row_num, returning 0\n");
#  		return 0;
#  	}
#  }
#
# struct Matrix mx_set(struct Matrix mx, int row, int col, double val){
#  	if(row == 0 || col == 0){
#  		printf("Error: mx_set array start with 1\n");
#  	}else if(row == 1){
#  		mx.x[col - 1] = val;
#  	}else if(row == 2){
#  		mx.y[col - 1] = val;
#  	}else if(row == 3){
#  		mx.z[col - 1] = val;
#  	}else if(row == 4){
# 		printf("Warning: mx_set, modifying constant row\n");
# 		//mx.one[col - 1] = val;
#  	}else{
#  		printf("Err: mx_row, invalid row_num, returning original matrix\n");
#  		return mx;
#  	}
#  	return mx;
#  }
#
# void mx_free(struct Matrix mx){
#  	if(mx.type == 'a'){
#  		if(mx.col != 0){
#  			free(mx.x);
#  			free(mx.y);
#  			free(mx.z);
#  		}
#  	}else if(mx.type == 'c'){
# 		if(mx.col != 0){
# 			free(mx.x);
# 			free(mx.y);
# 			free(mx.z);
# 			free(mx.vx);
# 			free(mx.vy);
# 			free(mx.vz);
# 		}
# 	}
#  }
#
# struct Matrix mx_copy(struct Matrix src, struct Matrix dst){
# 	if(src.type == 'b'){
# 		dst = mx_init_e(dst,src.col);
# 		int i;
# 		for(i = 0; i < src.col;i ++){
# 			dst.x[i] = src.x[i];
# 			dst.y[i] = src.y[i];
# 			dst.z[i] = src.z[i];
#
# 			i++;
#
# 			dst.x[i] = src.x[i];
# 			dst.y[i] = src.y[i];
# 			dst.z[i] = src.z[i];
#
# 			dst.edge_num ++;
# 		}
# 	}
# 	return dst;
# }
#
# void mx_export(struct Matrix mx, struct Light lt, int color[]){
# 	if(mx.type == 'a'){
# 		drawPoint(mx,color);
# 	}else if(mx.type == 'b'){
# 		//printf("Whj\n");
# 		printf("mx.z:%f\n",mx.z[1]);
# 		drawLine(mx,color);
# 	}else if(mx.type == 'c'){
# 		//drawLine(mx,color);
# 		//scanLine(mx);
# 		reflection(mx,lt);
# 		//drawPoint(mx,color);
# 	}
# }
#
# void db_export(struct Matrix mx){
# 	int color[3];
# 	color[0] = 255;
# 	color[1] = 0;
# 	color[2] = 0;
# 	if(mx.type == 'a'){
# 		drawPoint(mx,color);
# 	}else if(mx.type == 'b'){
# 		drawLine(mx,color);
# 	}else if(mx.type == 'c'){
# 		drawLine(mx,color);
# 		//drawPoint(mx,color);
# 	}
# }
