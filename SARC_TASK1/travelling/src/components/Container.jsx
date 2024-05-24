import "./Container.css"

export default function Container({clas,pic,Name,nclass}) {
    return <div className={clas}>

        <div className={pic}>
        
            
        </div>
        <div className ={nclass}>
           <p>{Name}</p> 
        </div>
    </div>
}